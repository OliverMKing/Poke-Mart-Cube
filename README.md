# Poké Mart Cube

> ## 👉 [Click here to see the cube](https://htmlpreview.github.io/?https://raw.githack.com/OliverMKing/Poke-Mart-Cube/main/site/index.html)
>
> **Start here.** This link opens the cube page in your browser.
> The page shows all 360 cards, the rules, the type summaries and the balance notes.
> You can search the cards, filter them by type or by set, and list them by set.

The Poké Mart Cube is a 360-card Pokémon Trading Card Game (TCG) cube for drafting.
Every card except one costs less than 10 US dollars (USD).
The exception is Supreme Victors Minun (about 26 USD). The cube uses it on purpose.
The full cube costs about 240 USD at TCGplayer market prices from October 2026.

The cube is on CubeKoga: <https://cubekoga.net/cube/pokemartcube/visual>.
The card checklist is a GitHub Issue: <https://github.com/OliverMKing/Poke-Mart-Cube/issues/1>. Tick a card there when you own it.

The cube is a singleton cube.
It has one copy of each card and one card for each Pokémon species.
Each Pokémon gives up one Prize card when it is Knocked Out.

## Format

The cube is for 6 players.
Each player opens 4 packs of 15 cards and picks 60 cards.
Each player builds a 50-card deck and plays with 5 Prize cards.
Basic Energy is not in the packs. Each player adds any number of Basic Energy cards to their deck.

| Players | Packs per player | Picks | Deck size | Prize cards |
|---|---|---|---|---|
| 6 (house rule) | 4 × 15 | 60 | 50 | 5 |
| 8 | 3 × 15 | 45 | 40 | 4 |
| 4 | 6 × 15 | 90 | 60 | 6 |

Every row uses all 360 cards.
The card list works for every row.
For 5-prize games, you can add some optional cards.
Read [docs/design-notes.md](docs/design-notes.md) for those cards.

## House rules

1. Use the current Standard rules for the first turn. The player who goes first cannot attack or play a Supporter.
2. Treat a Poké-Power or a Poké-Body as an Ability. This affects Claydol, Donphan, Porygon2, Sableye, Unown Q and Uxie.
3. Treat an old card that says only "Trainer" as an Item. This affects Pokémon Breeder.
4. Ignore text about Pokémon ex, V, GX, EX, Prism Star and Radiant cards. The cube has none of these cards. For example, Twin Energy always provides two Colorless Energy.
5. Brilliant Blender is the only ACE SPEC card in the cube. Its limit of one ACE SPEC card in each deck has no effect.
6. Remove a card in the Lost Zone from the game. Do not return it to play.

## Files

| Path | Contents |
|---|---|
| `cube/cube_list.py` | The card list. This file is the source of truth. |
| `cube/page_config.json` | Page text that the card data does not supply: type summaries, price limit, price exceptions, price overrides and excluded staples. It also holds the number of the checklist Issue. |
| `cube/cards.json` | Card text, statistics and price for each card. The build script makes this file. |
| `cube/cardlist.csv` | One row for each card, for spreadsheets. The build script makes this file. |
| `cube/cubekoga-import.tsv` | The list for the CubeKoga Bulk Import box. The build script makes this file. |
| `site/template.html` | The page design. |
| `site/index.html` | The cube page. The build script makes this file. Open it in a browser. |
| `scripts/build.py` | Checks the card list and makes all output files. |
| `scripts/search.py` | Finds cards and prices when you want to change a card. |
| `scripts/checklist.py` | Makes and updates the card checklist Issue on GitHub. |
| `scripts/cardapi.py` | The Pokémon TCG API client with a local cache. |
| `docs/design-notes.md` | Design decisions, balance notes and the change history. |
| `docs/research.md` | The research behind the card choices. |
| `archive/v1-playset/` | The first version of the cube, with multiple copies of each card. |

## Build the page

The scripts use Python 3.10 or later and the standard library only.

1. Open a terminal in the repository root.
2. Run `python3 scripts/build.py`.
3. Open `site/index.html` in a browser.

The build script reads card data from `.cache/`.
If a card is not in the cache, the script gets it from the Pokémon TCG API.
The script stops and lists each problem if the card list breaks a rule.

The script checks these rules:

- The cube has exactly 360 cards.
- Each card ID, card name and Pokémon species occurs one time only.
- Each card costs less than the price limit in `cube/page_config.json`. Cards in `price_exceptions` in the same file can cost more.
- Each card has a price. The price comes from the API, or from `price_overrides` in `cube/page_config.json` when the API has no price.
- Each evolution line is complete in its group.

## Update the prices

1. Run `python3 scripts/build.py --refresh`.
2. Read the result line. It shows the new total and the most expensive card.
3. If a card is now over the price limit, replace it. Use the procedure in the next section.
4. If the result line says that the API now has a price for a card, remove that card from `price_overrides` in `cube/page_config.json`.

A card from a new set can be on TCGplayer before the Pokémon TCG API has its price.
The build stops if a card has no price.
For each such card, add the TCGplayer market price to `price_overrides` in `cube/page_config.json`.
Record the product URL and the date that you checked the price.
The build uses an override price only while the API has no price for the card.

The API sometimes returns server errors. The script tries each request again.
If a request still fails, run the command again.
To get a higher rate limit, set the `POKEMONTCG_API_KEY` environment variable.

## Change a card

1. Find candidates with `python3 scripts/search.py <card name>`. Add `--full` to see the card text.
2. Edit `cube/cube_list.py`. Keep one Basic, one Stage 1 and one Stage 2 in each Stage 2 line.
3. Run `python3 scripts/build.py`.
4. Fix each problem that the script reports.
5. If the change affects a type summary, edit `cube/page_config.json`.
6. Add the change to the decision log in `docs/design-notes.md`.

## Track the cards you own

The card checklist is GitHub Issue #1: <https://github.com/OliverMKing/Poke-Mart-Cube/issues/1>.
Each card in the cube has a checkbox in the Issue.

1. Open the Issue.
2. Tick the box for each card that you own. GitHub saves each tick.

Only the repository owner and collaborators with write access can tick the boxes.

When the cube changes, update the Issue:

1. Run `python3 scripts/build.py`.
2. Run `python3 scripts/checklist.py update`.

The script writes the new card list into the Issue and keeps your ticks.
If you own a card that is not in the cube now, the script moves it to the "Cut from the cube" section.
To see the new text before you change the Issue, run `python3 scripts/checklist.py show`.
The script uses the GitHub CLI (`gh`). Log in with `gh auth login` first.

## Import the cube into CubeKoga

1. Open the cube on CubeKoga: <https://cubekoga.net/cube/pokemartcube/visual>.
2. Open the Bulk Import box.
3. Paste the contents of `cube/cubekoga-import.tsv`.

Each line has four values separated by tabs: quantity, name, set code and card number.
The set codes are Pokémon TCG API set IDs.

## Sources

- Build guidance and popularity data: [CubeKoga](https://cubekoga.net/articles/how-to-build-a-pokemon-cube).
- Card text and prices: [Pokémon TCG API](https://pokemontcg.io). The prices are TCGplayer market prices.

This is a fan project.
Pokémon and the Pokémon TCG are trademarks of their owners.
