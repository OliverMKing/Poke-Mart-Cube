#!/usr/bin/env python3
"""Keep a GitHub Issue with a checklist of every card in the cube.

Tick a box in the Issue when you own the card. GitHub saves the tick.
The Issue number is in cube/page_config.json (checklist_issue).

Usage:
  python3 scripts/checklist.py create   make the Issue and save its number
  python3 scripts/checklist.py update   rewrite the Issue for the current cube and keep the ticks
  python3 scripts/checklist.py show     print the text that update would write

Run scripts/build.py first, because this script reads cube/cards.json.
The script uses the GitHub CLI (gh). Log in with `gh auth login` first.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import TRAINERS, TYPES  # noqa: E402
from cardapi import ROOT  # noqa: E402

CONFIG = ROOT / 'cube' / 'page_config.json'
TITLE = 'Card checklist'
SECTIONS = TYPES + TRAINERS + ['Energy']
HEADINGS = {'Supporter': 'Supporters', 'Item': 'Items', 'Tool': 'Pokémon Tools', 'Stadium': 'Stadiums',
            'Energy': 'Special Energy'}
# One checklist line: "- [x] text <!-- card id -->". The hidden card ID keeps the tick when the text changes.
LINE = re.compile(r'^- \[([ xX])\] (.*?)\s*<!-- (\S+) -->$')
BODY_LIMIT = 65536  # GitHub's limit for an Issue body


def gh(*args, stdin=None):
    try:
        return subprocess.run(['gh', *args], cwd=ROOT, input=stdin, check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        sys.exit(f'gh {" ".join(args[:2])} failed: {e.stderr.strip()}')


def parse(body):
    """Return {card id: (ticked, text)} for each checklist line in an Issue body."""
    out = {}
    for line in body.splitlines():
        m = LINE.match(line.strip())
        if m:
            out[m.group(3)] = (m.group(1) != ' ', m.group(2))
    return out


def card_text(r):
    name = f'[{r["name"]}]({r["url"]})' if r['url'] else r['name']
    return f'{name} · {r["set"]} {r["number"]} · ${r["price"]:.2f}'


def render(rows, old):
    """Make the Issue body. Keep the ticks in old, and keep owned cards that left the cube."""
    def box(cid):
        return 'x' if old.get(cid, (False, ''))[0] else ' '

    parts = ['Tick a box when you own the card. GitHub saves the tick.', '',
             'The list follows `cube/cube_list.py`. After a cube change, run `python3 scripts/checklist.py update`. '
             'The script rewrites this text and keeps the ticks. Do not edit the text by hand.']
    for sec in SECTIONS:
        sec_rows = [r for r in rows if r['section'] == sec]
        parts += ['', f'## {HEADINGS.get(sec, sec)} ({len(sec_rows)})', '']
        parts += [f'- [{box(r["id"])}] {card_text(r)} <!-- {r["id"]} -->' for r in sec_rows]
    ids = {r['id'] for r in rows}
    cut = [(cid, text) for cid, (ticked, text) in old.items() if ticked and cid not in ids]
    if cut:
        parts += ['', f'## Cut from the cube ({len(cut)})', '', 'You own these cards, but they are not in the cube now.', '']
        parts += [f'- [x] {text} <!-- {cid} -->' for cid, text in cut]
    body = '\n'.join(parts) + '\n'
    if len(body) > BODY_LIMIT:
        sys.exit(f'The checklist has {len(body)} characters. GitHub allows {BODY_LIMIT} in an Issue.')
    return body


def current(cfg):
    n = cfg.get('checklist_issue')
    if not n:
        return None, {}
    return n, parse(json.loads(gh('issue', 'view', str(n), '--json', 'body'))['body'])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('command', choices=['create', 'update', 'show'])
    args = ap.parse_args()

    cfg = json.loads(CONFIG.read_text())
    rows = json.loads((ROOT / 'cube' / 'cards.json').read_text())

    if args.command == 'create':
        if cfg.get('checklist_issue'):
            sys.exit(f'Issue #{cfg["checklist_issue"]} already exists. Run update instead.')
        url = gh('issue', 'create', '--title', TITLE, '--body-file', '-', stdin=render(rows, {})).strip()
        cfg['checklist_issue'] = int(url.rsplit('/', 1)[1])
        CONFIG.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + '\n')
        print(f'Made {url}. Its number is in cube/page_config.json.')
        return

    n, old = current(cfg)
    body = render(rows, old)
    if args.command == 'show':
        print(body, end='')
        return
    if not n:
        sys.exit('cube/page_config.json has no checklist_issue. Run create first.')
    gh('issue', 'edit', str(n), '--body-file', '-', stdin=body)
    owned = sum(1 for r in rows if old.get(r['id'], (False, ''))[0])
    print(f'Updated Issue #{n}: you own {owned} of {len(rows)} cube cards.')


if __name__ == '__main__':
    main()
