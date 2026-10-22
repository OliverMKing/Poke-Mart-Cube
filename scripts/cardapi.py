"""Small client for the Pokémon TCG API (https://pokemontcg.io) with a local cache.

Card data and TCGplayer market prices come from https://api.pokemontcg.io/v2/cards.
Responses are cached under .cache/ so repeat builds do not hit the API.
Set POKEMONTCG_API_KEY to raise the API rate limit (optional).
"""
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache'
API = 'https://api.pokemontcg.io/v2/cards'
FIELDS = ('id,name,supertype,subtypes,hp,types,evolvesFrom,abilities,attacks,rules,'
          'tcgplayer,set,rarity,number,weaknesses,retreatCost,nationalPokedexNumbers,ancientTrait')


def _headers():
    h = {'User-Agent': 'pokemartcube'}
    if os.environ.get('POKEMONTCG_API_KEY'):
        h['X-Api-Key'] = os.environ['POKEMONTCG_API_KEY']
    return h


def _get(url, tries=6):
    """GET a JSON URL. The API sometimes returns 500/502, so retry with backoff."""
    err = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=_headers())
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - network errors of any kind are retried
            err = e
            time.sleep(2 + 3 * attempt)
    raise RuntimeError(f'GET {url} failed: {err}')


def fetch_card(card_id, refresh=False):
    """Return one card by API id, from the cache unless refresh is set."""
    path = CACHE / 'cards' / f'{card_id}.json'
    if path.exists() and not refresh:
        return json.loads(path.read_text())
    data = _get(f'{API}/{urllib.parse.quote(card_id)}')['data']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return data


def fetch_cards(ids, refresh=False, workers=6):
    """Fetch many cards in parallel. Returns {id: card}. Raises if any fetch fails."""
    out, failed = {}, []

    def one(i):
        try:
            return i, fetch_card(i, refresh)
        except RuntimeError as e:
            return i, e

    with ThreadPoolExecutor(workers) as ex:
        for i, res in ex.map(one, ids):
            if isinstance(res, Exception):
                failed.append((i, str(res)))
            else:
                out[i] = res
    if failed:
        raise RuntimeError(f'{len(failed)} card fetches failed, run again: {failed[:5]}')
    return out


def search(query, refresh=False):
    """Run an API search query (for example 'name:"Charizard"') and cache the result."""
    key = hashlib.md5(query.encode()).hexdigest()
    path = CACHE / 'search' / f'{key}.json'
    if path.exists() and not refresh:
        return json.loads(path.read_text())
    url = API + '?' + urllib.parse.urlencode({'q': query, 'pageSize': 250, 'select': FIELDS})
    data = _get(url)['data']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return data


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def _product_id(url, tries=4):
    """Read the TCGplayer product ID from the first redirect of a prices.pokemontcg.io link."""
    opener = urllib.request.build_opener(_NoRedirect)
    for attempt in range(tries):
        try:
            opener.open(urllib.request.Request(url, headers=_headers()), timeout=30)
        except urllib.error.HTTPError as e:
            m = re.search(r'tcgplayer\.com/product/(\d+)', urllib.parse.unquote(e.headers.get('Location') or ''))
            if m:
                return m.group(1)
            if e.code < 500:
                return None
        except Exception:  # noqa: BLE001 - network errors of any kind are retried
            pass
        time.sleep(2 + 3 * attempt)
    return None


def tcgplayer_url(card):
    """Direct link to the card's TCGplayer product page, or the API link if the product is unknown.

    The API link redirects through affiliate trackers, which ad blockers often block.
    The product ID is cached under .cache/tcgplayer/.
    """
    url = (card.get('tcgplayer') or {}).get('url')
    if not url:
        return None
    path = CACHE / 'tcgplayer' / f'{card["id"]}.txt'
    if path.exists():
        pid = path.read_text().strip()
    else:
        pid = _product_id(url)
        if not pid:
            return url
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(pid)
    return f'https://www.tcgplayer.com/product/{pid}'


def tcgplayer_urls(cards, workers=8):
    """Return {card id: tcgplayer_url(card)} for many cards, fetched in parallel."""
    cards = list(cards)
    with ThreadPoolExecutor(workers) as ex:
        return dict(zip((c['id'] for c in cards), ex.map(tcgplayer_url, cards)))


def min_price(card):
    """Cheapest TCGplayer market price over the card's versions (normal, holo, reverse holo).

    Returns (price, version) or (None, None) when TCGplayer has no price.
    """
    prices = (card.get('tcgplayer') or {}).get('prices') or {}
    vals = [(v.get('market') or v.get('mid'), k) for k, v in prices.items() if (v.get('market') or v.get('mid'))]
    return min(vals) if vals else (None, None)


def card_text(card):
    """Readable card text: abilities and attacks for Pokémon, rules text for the rest."""
    if card['supertype'] != 'Pokémon':
        return list(card.get('rules') or [])
    lines = []
    if card.get('ancientTrait'):
        t = card['ancientTrait']
        lines.append(f"<Ancient Trait: {t.get('name', '')}> {t.get('text', '')}")
    for a in card.get('abilities') or []:
        lines.append(f"<{a.get('type')}: {a['name']}> {a.get('text', '')}")
    for a in card.get('attacks') or []:
        cost = ''.join(x[0] if x != 'Colorless' else 'C' for x in a.get('cost', []))
        lines.append(f"[{cost}] {a['name']} {a.get('damage', '')}: {a.get('text', '')}")
    return lines
