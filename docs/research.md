# Research

This document records the research behind the card choices.
The research was done on 2026-10-21.

## CubeKoga build guidance

CubeKoga is a website for Pokémon Trading Card Game (TCG) cubes.
Its guide [How to Build a Pokémon Cube](https://cubekoga.net/articles/how-to-build-a-pokemon-cube) gives this guidance:

- Start with 360 cards for a first cube. This size supports 4 to 6 players and divides cleanly into packs.
- Use about 50% to 55% Pokémon, 40% to 45% Trainers and 5% to 10% Energy. Most cubes supply Basic Energy free, so only Special Energy takes cube slots.
- Keep each evolution line complete. If a Stage 2 is in the cube, its Stage 1 and Basic must also be in the cube.
- Use the same line sizes for all lines, so that new players learn the ratios one time. Example ratios for a Stage 2 line are 6-5-4, 4-3-2 and 1-1-1 ("Chaos").
- Give each type about the same number of cards and a clear reason to draft it.
- Include support Pokémon that help any deck, because drafters fight for them.
- Do not use narrow combo cards. A random draft rarely gives a player all the parts.

The guide [How to Draft a Pokémon Cube](https://cubekoga.net/articles/how-to-draft-a-pokemon-cube) gives this setup for a 360-card cube:

| Players | Packs per player | Cards per pack | Deck size | Prize cards |
|---|---|---|---|---|
| 4 | 6 | 15 | 60 | 6 |
| 6 | 4 | 15 | 50 | 5 |
| 8 | 3 | 15 | 40 | 4 |

It also suggests these deck counts:

| Deck size | Pokémon | Trainers | Energy |
|---|---|---|---|
| 40 cards | 12 to 14 | 11 to 15 | 9 to 11 |
| 60 cards | 18 to 21 | 17 to 22 | 13 to 17 |

## CubeKoga popularity data

The CubeKoga statistics pages use data from 3,487 public cubes.
The values below show the share of public cubes that include each card.

**Pokémon cards:** Ditto ◇ (Lost Thunder) 26.4%, Lapras (Legend Maker) 19.5%, Alolan Vulpix (Guardians Rising) 19.2%, Uxie (Legends Awakened) 18.8%, Kirlia (Silver Tempest) 18.2%, Pidgeotto (Team Up) 17.8%, Azelf (Legends Awakened) 16.7%, Jirachi (Team Up) 16.6%, Octillery (BREAKthrough) 15.7%, Bronzong (Phantom Forces) 14.9%.

**Evolution lines:** Ninetales 47.9%, Eevee lines 44.9%, Raichu 43.7%, Magnezone 42.7%, Gardevoir 39.6%, Ampharos 35.8%, Machamp 31.9%, Metagross 31.6%.

**Trainers:** Switch 69.6%, Ultra Ball 59.1%, Rare Candy 52.3%, Super Rod 49.1%, Nest Ball 48.9%, Great Ball 48.1%, Escape Rope 47.8%, Judge 47.5%.

**Special Energy:** Rainbow Energy 50.1%, Double Colorless Energy 47.2%, Capture Energy 31.7%, Counter Energy 28.6%, Aurora Energy 27.0%, Jet Energy 26.8%.

## Reference cubes

The 127 most-liked public cubes on CubeKoga were the source for card popularity and card text.
Two cubes were the main references:

- **Noah's Ark** is the most-liked cube on CubeKoga. It has 360 cards and a low-to-mid power level. It uses 8 players, 3 packs of 15 cards, 40-card decks and 4 Prize cards. Each evolution line has two different cards for each stage.
- **Chaos Cube** is the most-liked singleton cube. It has 480 cards: 247 Pokémon, 214 Trainers and 19 Energy. Its Pokémon are 132 Basic, 72 Stage 1 and 21 Stage 2 cards. The Poké Mart Cube uses a similar Basic-heavy mix.

## Price data

The prices are TCGplayer market prices from the [Pokémon TCG API](https://pokemontcg.io).
The API updated the prices on 2026-10-15.
Each card uses the price of its cheapest version, such as non-holo, holo or reverse holo.

Do not use the prices that CubeKoga stores with each card.
Many of them are out of date. For example, CubeKoga shows Ditto ◇ at 3.68 US dollars (USD). Its market price is 50.08 USD.

## Data access notes

The CubeKoga website loads its data from a JSON API.
These endpoints were useful:

| Endpoint | Data |
|---|---|
| `https://cubekoga.net/api/articles` | List of articles |
| `https://cubekoga.net/assets/articles/<slug>.md` | Article text in Markdown |
| `https://cubekoga.net/api/stats/pokemon?take=50` | Most-included Pokémon cards (also `/lines`, `/trainers`, `/energy`) |
| `https://cubekoga.net/api/cubes/all?skip=0&take=60&sort=likes` | Public cubes, most-liked first |
| `https://cubekoga.net/api/cubes/cube/<id>` | Cube details and rules text |
| `https://cubekoga.net/api/cubes/<id>/cards` | Card list for a cube |

The Pokémon TCG API sometimes returns HTTP 500 and 502 errors.
The scripts in this repository try each request again and keep a local cache in `.cache/`.
