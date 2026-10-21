# Design notes

This document records why the cube looks the way it does.
Read it before you change cards.

## Goals

The cube has four goals:

1. Each card costs less than 10 US dollars (USD).
2. The cube is fun and interesting to draft. It uses popular cube cards where the price limit allows.
3. The types are balanced. Each type has a real deck in it.
4. The cube is a singleton cube. It has one copy of each card and one card for each Pokémon species.

## Structure

Each type has the same shape:

| Part | Count | Cards |
|---|---|---|
| Stage 2 lines | 2 | 6 (one Basic, one Stage 1 and one Stage 2 in each line) |
| Stage 1 lines | 4 | 8 (one Basic and one Stage 1 in each line) |
| Basics without an evolution | 7 | 7 |
| Total | | 21 |

The cube uses eight types: Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness and Metal.
Colorless has one more Basic, so it has 22 cards.
The cube does not use the Dragon and Fairy types.

The Pokémon are 117 Basic, 54 Stage 1 and 19 Stage 2 cards.
The Psychic Kirlia has two Stage 2 options, Gardevoir and Gallade. The player who drafts Kirlia chooses between them.
This Basic-heavy mix follows Chaos Cube.
Chaos Cube is the most-liked singleton cube on CubeKoga.

## Card mix

| Category | Cards | Share |
|---|---|---|
| Pokémon | 190 | 53% |
| Supporters | 59 | 16% |
| Items | 62 | 17% |
| Pokémon Tools | 15 | 4% |
| Stadiums | 9 | 3% |
| Special Energy | 25 | 7% |

The CubeKoga build guide recommends 50% to 55% Pokémon, 40% to 45% Trainers and 5% to 10% Energy.
The cube is inside each range.

## Card selection principles

- **Single-prize Pokémon only.** Each Knockout gives one Prize card. This keeps the Prize race the same for all decks.
- **Modern attackers, classic support.** Most attackers come from Sun and Moon, Sword and Shield and Scarlet and Violet. Their damage and Hit Points (HP) are in the same range. Some older support cards are also in the cube, such as Claydol, Porygon2 and Sableye. They are weak attackers, so they do not change the damage range.
- **No functional reprints.** The cube has no two cards with the same effect under different names. For example, Professor's Research is in the cube, but Professor Juniper and Professor Sycamore are not.
- **Cheapest version.** The price for each card is the TCGplayer market price of its cheapest version. Usually this is the non-holo version.

## How the types stay level

- Each type has at least one draw or search engine. Each type also has at least one way to accelerate Energy.
- The biggest attacks have a cost. Some attacks discard Energy, some attacks prevent an attack on the next turn, and some attacks damage the attacker.
- Most Stage 2 Pokémon have 150 to 180 HP.
- Darkness and Psychic have the lowest fixed damage. Each tops out at 160: Mightyena for Darkness and Gallade for Psychic.
- Darkness makes up for this with attacks that grow during the game: Zoroark, Spiritomb and Galarian Moltres. It also places damage counters with Galarian Zigzagoon, Galarian Obstagoon and Absol.
- Psychic attacks with Gallade (160), Dusknoir (150) and Mewtwo (90, or 180 when the opponent has 3 or fewer Prize cards left). Mesprit hits for 160 when Uxie and Azelf are on the Bench.
- 17 Special Energy cards provide more than one type. They help decks that use two types. Crispin also helps.

## Finishing evolution lines

In a singleton cube, each evolution line has only one card for each stage.
These cards help a player finish a line:

- Rare Candy, Pokémon Breeder, Wally and Evosoda evolve a Pokémon without the usual steps.
- Evolution Incense, Timer Ball, Capturing Aroma, Jacq, Hilda and Kangaskhan find Evolution cards.

With 6 players, each 15-card pack comes back to each player two times, at picks 7 and 13.
A player who takes a Stage 2 from a pack often gets its Basic and Stage 1 back from the same pack.

## Weakness coverage

This table shows how many Pokémon cards in the cube take double damage from each type.
The page calculates this table again each time you build it. Update this copy after card changes.

| Attacking type | Pokémon hit for double damage | Main targets |
|---|---|---|
| Fighting | 40 | Lightning 20, Colorless 14, Darkness 6 |
| Fire | 39 | Grass 21, Metal 18 |
| Lightning | 27 | Water 13, Colorless 6, Darkness 4, Metal 3, Lightning 1 |
| Water | 23 | Fire 21, Fighting 2 |
| Grass | 20 | Darkness 9, Fighting 7, Water 4 |
| Darkness | 16 | Psychic 16 |
| Psychic | 13 | Fighting 11, Psychic 2 |
| Metal | 6 | Water 4, Psychic 2 |

Fighting and Fire have the widest coverage.
Weakness Policy and Coating Metal Energy are the counters in the cube.

## Watch list

Check these points after the first drafts:

1. **Fire speed.** Stoke, Burn Brightly, Chi-Yu and the 240-damage Arcanine can end games quickly. Five-prize games give slower decks more time.
2. **Weakness coverage.** Fighting and Fire each hit about 40 Pokémon for double damage.
3. **Damage counters on the Bench.** Dusclops, Dusknoir, Obstagoon, Absol and Hawlucha can Knock Out small support Pokémon. Machoke prevents damage and damage counters on the Bench. Shaymin and Manaphy prevent attack damage to the Bench.
4. **Cofagrigus.** Law of the Underworld puts 6 damage counters on each Pokémon with an Ability, on both sides, for one Energy. Check how often it decides games.
5. **Hex Maniac.** It turns off all Abilities for one turn. The cube has many Ability engines, so this card is strong.
6. **Bench limits.** Sudowoodo and Collapsed Stadium limit each Bench to four Pokémon. Decks with four evolution lines feel this limit more.
7. **Darkness damage.** The best fixed Darkness attack is Mightyena's 160. If Darkness decks lose often, replace Sword and Shield Galarian Obstagoon (swsh1-119) with Champion's Path Galarian Obstagoon (swsh35-37). The Champion's Path card hits for 180.

## Cards left out

### Over the price limit

These popular cube cards cost more than 10 USD on 2026-10-21:

| Card | Printing | Price (USD) | Replacement in the cube |
|---|---|---|---|
| Ditto ◇ | Lost Thunder 154 | 50.08 | 151 Ditto |
| Lapras | Legend Maker 8 | 53.51 | 151 Lapras (Hop on My Back) |
| Uxie | Legends Awakened 43 | 18.67 | Astral Radiance Uxie (Wise Guidance) |
| Pidgeot | FireRed and LeafGreen 10 | 17.95 | Team Up Pidgeotto (Air Mail) |
| Shaymin | HeartGold and SoulSilver Unleashed 8 | 15.46 | Destined Rivals Shaymin |
| Azelf | Legends Awakened 19 | 10.88 | Surging Sparks Azelf |
| Jirachi | Team Up 99 | 10.59 | Stellar Crown Jirachi |

### Prize-count bonuses

Some cards get a bonus when a player has 4 or fewer Prize cards left.
In 4-prize games, this bonus is active from the first turn.
For this reason, these cards are not in the cube:

- Kartana (Unbroken Bonds): 130 damage for one Energy with exactly 4 Prize cards left.
- Gouging Fire (Surging Sparks)
- Lacey
- Roxanne

In 5-prize games, the bonus starts only after the first Knockout.
You can add these cards back for 5-prize games.

### Abilities that do nothing in this cube

- Twilight Masquerade Thwackey. Its Ability needs the Festival Lead Ability.
- Ultra Prism Pachirisu. Its attack needs Benched Pokémon with the Nuzzle attack.
- Shining Legends Pokémon Breeder. It has the same name as the Base Set card, but a different effect. The cube uses the Base Set 2 card.

### Weak in a singleton cube

- Twilight Masquerade Drifblim. Its damage counts Drifloon and Drifblim in play. A singleton cube has only one of each.

## Lost Zone cards

Two cards use the Lost Zone: Faba and Lost Vacuum.
None of them is a Lost Zone payoff, and the cube has no Lost Zone strategy.

- Faba removes a Tool, Special Energy or Stadium permanently. Cards in the Lost Zone cannot come back, so Faba beats Recycle Energy and Lusamine.
- Lost Vacuum removes a Tool or Stadium. The cost is one card from your hand.

## Decision log

| Date | Decision |
|---|---|
| 2026-10-21 | Built version 1: 360 cards with multiple copies of each card, 8 players, 40-card decks and 4 Prize cards. This version is in `archive/v1-playset/`. |
| 2026-10-21 | Changed to a singleton cube: one copy of each card and one card for each Pokémon species. |
| 2026-10-21 | Removed Kartana, Gouging Fire, Lacey and Roxanne because of the 4-prize bonus problem. Replaced Thwackey, Pachirisu, Drifblim and the Shining Legends Pokémon Breeder. |
| 2026-10-21 | Changed the main format to 6 players, 4 packs of 15 cards, 50-card decks and 5 Prize cards. The card list did not change. |
| 2026-10-21 | Decided not to add Regigigas. The Astral Radiance Regigigas needs all five Regis in play, and the cube has only three. In a singleton draft, it would almost never work. |
| 2026-10-21 | Kept the three Lost Zone cards. They are in the cube for their main effects. |
| 2026-10-21 | Replaced Vivid Voltage Donphan (swsh4-87) with Lost Thunder Donphan (sm8-112). The old card did 120 damage for one Energy on a 150-HP Stage 1, and Fighting already hits 40 Pokémon for double damage. The new card has Sturdy and a Rolling Spin attack that does 70, then 140 on the next turn. |
| 2026-10-21 | Replaced Lost Thunder Donphan (sm8-112) with Donphan Prime. The cube uses the Celebrations Classic Collection reprint (cel25c-107_A, about 1.50 USD) because the HeartGold and SoulSilver original costs about 41 USD. Exoskeleton is a Poké-Body, so the house rule treats it as an Ability. |
| 2026-10-21 | Gave Psychic a real attacker. Added Astral Radiance Gallade (swsh10-62), which evolves from the existing Kirlia. Replaced Unbroken Bonds Mewtwo (sm10-75) with Crown Zenith Mewtwo (swsh12pt5-59). Removed Comfey to keep Psychic at 21 cards. |
| 2026-10-21 | Replaced Temporal Forces Centiskorch (sv5-37) with Mega Evolution Centiskorch (me1-30). The old card's 180-damage attack needed the opponent's Active Pokémon to be Burned, and its own Singe attack was the only Burn source in the cube. The new card has Coiling Crush (50 damage, flip 2 coins, discard an Energy for each heads) and Heat Crawler (140). |
| 2026-10-21 | Replaced the Sizzlipede and Centiskorch line with a Salandit (swsh12pt5-27) and Salazzle (sv7-24) line. Salazzle is a medium-strength Fire attacker: Flamethrower does 130, and Sudden Scorching makes the opponent discard 1 card, or 3 cards on the turn that Salazzle evolves. |
| 2026-10-21 | Made Darkness stronger. Replaced Temporal Forces Mightyena (sv5-106, 130 damage for three Energy) with Astral Radiance Mightyena (swsh10-96). Its Wild Tackle does 160 for three Colorless Energy and 50 damage to itself. |
| 2026-10-21 | Replaced the Shuppet and Banette line with a Yamask (sv4-75) and Cofagrigus (sv8-83) line as a spread payoff. Cofagrigus's Law of the Underworld puts 6 damage counters on each Pokémon with an Ability, on both sides, for one Energy. Yamask's Ominous Eyes puts 3 damage counters on one of the opponent's Pokémon. |

## Options

These changes are possible. They are not in the cube now.

- **Add the 4-prize cards back.** For 5-prize games, add Kartana, Gouging Fire, Lacey or Roxanne.
- **Regi package.** Add Stormfront Regigigas (about 7 USD) and Astral Radiance Regice. Replace Regirock with the Astral Radiance Regirock, which has Regi Gate. Stormfront Regigigas is a weak card, so this package is for fun only.
- **Remove the Lost Zone.** Replace Lost Vacuum and Faba with other removal cards.
