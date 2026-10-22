#!/usr/bin/env python3
"""Check the cube list and build every output file.

Reads   cube/cube_list.py, cube/page_config.json, site/template.html
Writes  cube/cards.json          card text, stats and price for every card
        cube/cardlist.csv        one row per card, for spreadsheets
        cube/cubekoga-import.tsv paste into CubeKoga's Bulk Import box
        site/index.html          the cube page

Usage:
  python3 scripts/build.py            build from cached card data
  python3 scripts/build.py --refresh  fetch fresh card data and prices first
"""
import argparse
import collections
import csv
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cardapi import ROOT, card_text, fetch_cards, min_price, tcgplayer_urls  # noqa: E402

TYPES = ['Grass', 'Fire', 'Water', 'Lightning', 'Psychic', 'Fighting', 'Darkness', 'Metal', 'Colorless']
TRAINERS = ['Supporter', 'Item', 'Tool', 'Stadium']
# Prefixes that do not make a different species (Galarian Zigzagoon is still Zigzagoon).
SPECIES_PREFIX = re.compile(r"^(Galarian|Alolan|Hisuian|Paldean|Team Rocket's|Ethan's|Misty's|Dark|Light) ")


def load_list():
    spec = importlib.util.spec_from_file_location('cube_list', ROOT / 'cube' / 'cube_list.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.P


def species(name):
    return re.sub(r' \[.*\]$', '', SPECIES_PREFIX.sub('', name))


def resolve(entries, cards, overrides=None, links=None):
    overrides, links = overrides or {}, links or {}
    rows = []
    for cid, count, section, line, note in entries:
        c = cards[cid]
        price, version = min_price(c)
        tcg = c.get('tcgplayer') or {}
        url, source = links.get(cid, tcg.get('url')), 'api'
        # A new set can be on TCGplayer before the API has its prices. Use the checked price until then.
        if price is None and cid in overrides:
            o = overrides[cid]
            price, version, url, source = o['price'], o['version'], o['url'], 'override'
        rows.append(dict(
            id=cid, count=count, section=section, line=line, note=note,
            name=c['name'], supertype=c['supertype'], subtypes=c.get('subtypes') or [],
            hp=c.get('hp'), types=c.get('types') or [], evolvesFrom=c.get('evolvesFrom'),
            price=price, variant=version, set=c['set']['name'], setid=c['set']['id'],
            number=c['number'], year=c['set'].get('releaseDate', '')[:4], released=c['set'].get('releaseDate', ''),
            series=c['set'].get('series', ''), text=card_text(c),
            weak=[w['type'] + w['value'] for w in c.get('weaknesses') or []],
            retreat=len(c.get('retreatCost') or []), rarity=c.get('rarity'),
            url=url, updated=tcg.get('updatedAt'), price_source=source))
    return rows


def check(rows, cfg):
    """Return a list of problems. An empty list means the cube passes."""
    problems = []
    total = sum(r['count'] for r in rows)
    if total != cfg['cube_size']:
        problems.append(f'cube has {total} cards, expected {cfg["cube_size"]}')
    for label, key in (('card id', lambda r: r['id']), ('card name', lambda r: r['name'])):
        dupes = [k for k, n in collections.Counter(key(r) for r in rows).items() if n > 1]
        if dupes:
            problems.append(f'duplicate {label}: {dupes}')
    if any(r['count'] != 1 for r in rows):
        problems.append('singleton cube: every count must be 1')
    mons = [r for r in rows if r['supertype'] == 'Pokémon']
    dupes = [k for k, n in collections.Counter(species(r['name']) for r in mons).items() if n > 1]
    if dupes:
        problems.append(f'duplicate Pokémon species: {dupes}')
    for r in rows:
        if r['price'] is None:
            problems.append(f'{r["id"]} {r["name"]}: no TCGplayer price')
        elif r['price'] >= cfg['price_limit'] and r['id'] not in cfg.get('price_exceptions', {}):
            problems.append(f'{r["id"]} {r["name"]}: ${r["price"]} is over the limit')
    by_line = collections.defaultdict(set)
    for r in mons:
        by_line[(r['section'], r['line'])].add(r['name'])
    for r in mons:
        if r['evolvesFrom'] and r['evolvesFrom'] not in by_line[(r['section'], r['line'])]:
            problems.append(f'{r["id"]} {r["name"]} evolves from {r["evolvesFrom"]}, which is not in its line')
        if r['section'] not in TYPES:
            problems.append(f'{r["id"]} {r["name"]} is a Pokémon in section {r["section"]}')
    return problems


def over_limit(rows, cfg):
    return [r for r in rows if r['price'] >= cfg['price_limit']]


def price_claim(rows, cfg):
    over = over_limit(rows, cfg)
    limit = f"${cfg['price_limit']:g}"
    if not over:
        return f'every card under {limit}'
    return f"all but {len(over)} card{'s' if len(over) > 1 else ''} under {limit}"


def price_note(rows, cfg):
    over = over_limit(rows, cfg)
    if not over:
        return ''
    names = ', '.join(f"{html.escape(r['set'])} {html.escape(r['name'])} (${r['price']:.2f})" for r in over)
    return f' {names} is over the ${cfg["price_limit"]:g} limit on purpose.'


def write_outputs(rows, cfg):
    (ROOT / 'cube' / 'cards.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False))

    with open(ROOT / 'cube' / 'cardlist.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['section', 'line', 'name', 'set', 'number', 'api_id', 'price_usd', 'version', 'note'])
        for r in rows:
            w.writerow([r['section'], r['line'], r['name'], r['set'], r['number'], r['id'],
                        f'{r["price"]:.2f}', r['variant'], r['note']])

    # CubeKoga matches set code + number against its card IDs, which are the API IDs.
    # Take the number from the ID, because a few IDs differ from the printed number (cel25c-107_A).
    tsv = '\n'.join(f'{r["count"]}\t{r["name"]}\t{r["setid"]}\t{r["id"].rsplit("-", 1)[1]}' for r in rows)
    (ROOT / 'cube' / 'cubekoga-import.tsv').write_text(tsv + '\n')

    n = sum(r['count'] for r in rows)
    total = sum(r['count'] * r['price'] for r in rows)
    npk = sum(r['count'] for r in rows if r['section'] in TYPES)
    ntr = sum(r['count'] for r in rows if r['section'] in TRAINERS)
    nen = sum(r['count'] for r in rows if r['section'] == 'Energy')
    top = max(rows, key=lambda r: r['price'])
    sec_count = collections.Counter()
    for r in rows:
        sec_count[r['section']] += r['count']
    data = [dict(i=r['id'], n=r['count'], s=r['section'], l=r['line'], note=r['note'], name=r['name'],
                 st=r['subtypes'], hp=r['hp'], ty=(r['types'] or [''])[0], ef=r['evolvesFrom'], p=r['price'],
                 v=r['variant'], set=r['set'], no=r['number'], y=r['year'], w=r['weak'], tx=r['text'],
                 url=r['url'], sid=r['setid'], rd=r['released'], se=r['series']) for r in rows]
    arch = {k: [v['headline'], v['summary']] for k, v in cfg['archetypes'].items()}
    excl = ''.join(
        f'<li><span class="xname">{html.escape(e["name"])}</span> <span class="xset">{html.escape(e["printing"])}</span> '
        f'<span class="tag tag-over">${e["price"]:.2f}</span></li>' for e in cfg['excluded_staples'])
    rep = {
        '__DATA__': json.dumps(data, ensure_ascii=False), '__TSV__': html.escape(tsv), '__TOTAL__': f'{total:,.2f}',
        '__NCARDS__': str(n), '__NPK__': str(npk), '__NTR__': str(ntr), '__NEN__': str(nen),
        '__TOPNAME__': html.escape(top['name']), '__TOPSET__': html.escape(f'{top["set"]} {top["number"]}'),
        '__TOPPRICE__': f'{top["price"]:.2f}', '__AVG__': f'{total / n:.2f}',
        '__UNDER1__': str(sum(r['count'] for r in rows if r['price'] < 1)),
        '__UPD__': max((r['updated'] or '') for r in rows).replace('/', '-'),
        '__ARCH__': json.dumps(arch, ensure_ascii=False), '__SECCOUNT__': json.dumps(sec_count),
        '__EXCL__': excl, '__PKPCT__': f'{npk / n * 100:.0f}', '__TRPCT__': f'{ntr / n * 100:.0f}',
        '__ENPCT__': f'{nen / n * 100:.0f}', '__PRICE_CLAIM__': price_claim(rows, cfg), '__PRICE_NOTE__': price_note(rows, cfg)}
    page = (ROOT / 'site' / 'template.html').read_text()
    for k, v in rep.items():
        page = page.replace(k, v)
    (ROOT / 'site' / 'index.html').write_text(page)
    return n, total, npk, ntr, nen, top


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--refresh', action='store_true', help='fetch fresh card data and prices from the API')
    args = ap.parse_args()

    cfg = json.loads((ROOT / 'cube' / 'page_config.json').read_text())
    entries = load_list()
    cards = fetch_cards([e[0] for e in entries], refresh=args.refresh)
    overrides = cfg.get('price_overrides', {})
    links = tcgplayer_urls(cards.values())
    rows = resolve(entries, cards, overrides, links)
    problems = check(rows, cfg)
    if problems:
        print('The cube list has problems:')
        for p in problems:
            print('  -', p)
        sys.exit(1)
    n, total, npk, ntr, nen, top = write_outputs(rows, cfg)
    print(f'OK: {n} cards ({npk} Pokémon, {ntr} Trainers, {nen} Special Energy), total ${total:,.2f}, '
          f'priciest {top["name"]} ${top["price"]:.2f}')
    for r in over_limit(rows, cfg):
        print(f'Note: {r["name"]} ({r["id"]}) is over the price limit at ${r["price"]:.2f}. It is in price_exceptions.')
    for r in rows:
        if r['price_source'] == 'override':
            print(f'Note: {r["name"]} ({r["id"]}) has no API price. The build uses ${r["price"]:.2f} from price_overrides.')
    unresolved = [r['id'] for r in rows if r['url'] and 'tcgplayer.com/product/' not in r['url']]
    if unresolved:
        print(f'Note: {len(unresolved)} cards link through the API redirect, because their TCGplayer product is unknown: '
              f'{unresolved[:5]}')
    for cid in overrides:
        if cid in cards and min_price(cards[cid])[0] is not None:
            print(f'Note: the API now has a price for {cid}. Remove it from price_overrides.')


if __name__ == '__main__':
    main()
