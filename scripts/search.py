#!/usr/bin/env python3
"""Search the Pokémon TCG API to find cards for the cube.

Prints one line per distinct card text, with the cheapest printing and its price.
By default it hides rule-box Pokémon (ex, V, GX, EX, Radiant and similar) and cards
printed before 2016, because the cube does not use them.

Examples:
  python3 scripts/search.py Charmander Charmeleon Charizard
  python3 scripts/search.py --since 2004 --full Pidgeot
  python3 scripts/search.py --rulebox "Regigigas"
  python3 scripts/search.py 'name:"Rare Candy"'
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cardapi import card_text, min_price, search  # noqa: E402

RULE_BOX = re.compile(r'( ex| EX|-EX|-GX| GX| V$| VMAX| VSTAR| V-UNION|LV\.X|BREAK|Radiant|TAG TEAM|MEGA|Prism Star|ACE SPEC)')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('names', nargs='+', help='card names, or raw API queries that contain a colon')
    ap.add_argument('--since', default='2016', help='earliest set release year to show (default 2016)')
    ap.add_argument('--rulebox', action='store_true', help='also show rule-box and ACE SPEC cards')
    ap.add_argument('--full', action='store_true', help='print the full card text')
    ap.add_argument('--refresh', action='store_true', help='ignore the cache')
    args = ap.parse_args()

    for name in args.names:
        query = name if ':' in name else f'name:"{name}"'
        groups = {}
        for c in search(query, args.refresh):
            if c['set'].get('releaseDate', '')[:4] < args.since:
                continue
            tags = c['name'] + ' ' + ' '.join(c.get('subtypes') or [])
            if not args.rulebox and RULE_BOX.search(tags):
                continue
            text = card_text(c)
            groups.setdefault((c['name'], c.get('hp'), '|'.join(text)), []).append(c)
        print(f'## {name}')
        for (_, hp, text), cards in groups.items():
            priced = [(min_price(c)[0], c) for c in cards if min_price(c)[0] is not None]
            price, c = min(priced, key=lambda x: x[0]) if priced else (None, cards[0])
            stage = ','.join(s for s in (c.get('subtypes') or []) if s != 'Basic') or 'Basic'
            kind = (c.get('types') or [c['supertype']])[0]
            short = ' / '.join((t[:t.index('>') + 1] if t.startswith('<') else re.sub(r':.*', '', t))[:40]
                               for t in text.split('|')) if text else ''
            print(f'  {c["id"]:14} {c["name"][:22]:22} {stage[:14]:14} hp{str(hp or "-"):>4} {kind[:9]:9} '
                  f'${price} | {short[:110]}')
            if args.full:
                for t in text.split('|'):
                    print('        ' + t)


if __name__ == '__main__':
    main()
