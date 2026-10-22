# Design notes

This document records why the cube looks the way it does.
Read it before you change cards.

## Goals

The cube has four goals:

1. Each card costs less than 10 US dollars (USD). Supreme Victors Minun (about 26 USD) is the one exception, by choice.
2. The cube is fun and interesting to draft. It uses popular cube cards where the price limit allows.
3. The types are balanced. Each type has a real deck in it.
4. The cube is a singleton cube. It has one copy of each card and one card for each Pokémon species.

## Structure

Most types have the same shape:

| Part | Count | Cards |
|---|---|---|
| Stage 2 lines | 2 | 6 (one Basic, one Stage 1 and one Stage 2 in each line) |
| Stage 1 lines | 4 | 8 (one Basic and one Stage 1 in each line) |
| Basics without an evolution | 7 | 7 |
| Total | | 21 |

The cube uses eight types: Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness and Metal.
Fighting has three Stage 2 lines, three Stage 1 lines and six Basics. It still has 21 cards.
Water has two Stage 2 lines, five Stage 1 lines and five Basics. It also has 21 cards.
Colorless has one more Basic, so it has 22 cards.
The cube does not use the Dragon and Fairy types.

The Pokémon are 115 Basic, 55 Stage 1 and 20 Stage 2 cards.
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
| Stadiums | 10 | 3% |
| Special Energy | 24 | 7% |

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
- Darkness and Psychic have the lowest fixed damage, at 160. Gallade hits for 160, and Mewtwo hits for 180 when the opponent has 3 or fewer Prize cards left. Mesprit hits for 160 when Uxie and Azelf are on the Bench.
- Psychic makes up for this with damage counters. Dusclops, Yamask and Cofagrigus place them, and Dusknoir moves them to score Knockouts.
- Darkness hits for 160 with Mightyena. Its attacks that grow during the game (Zoroark, Spiritomb and Galarian Moltres) add more damage, and Galarian Zigzagoon, Galarian Obstagoon and Absol place damage counters.
- 11 Special Energy cards can provide more than one type. They help decks that use two types. Crispin also helps.

## Strategies beyond attacking

The cube supports two slower strategies.

**Control** wins by milling, which means discarding cards from the opponent's deck until they cannot draw.

- Mill: Bunnelby (Ω Barrage lets it attack twice, so it can mill 2 cards each turn), Durant and Garganacl.
- Hand disruption: Salazzle and the hand resets from Judge, N, Iono and Marnie.
- Energy removal: Plumeria, Team Flare Grunt, Crushing Hammer, Enhanced Hammer and Faba.
- Other disruption: Celebi (Time Spiral devolves an opponent's Pokémon), Klefki (Memory Lock stops one of the opponent's attacks for a turn) and Hex Maniac.

**Tank and heal** decks wear the opponent down.

- Healing Pokémon: Garganacl (heals 20 from each of your Pokémon every turn), Blissey (fully heals a Benched Pokémon) and Miltank.
- Hard-to-damage Pokémon: Donphan, Scizor, Zamazenta, Copperajah and Blissey (200 HP).
- Healing Trainers: Max Potion, Hyper Potion, Super Potion, Pokémon Center Lady, Leftovers and Acerola.

## Discard synergy

Battle Compressor and Brilliant Blender put cards from your deck into your discard pile.
Many cards in the cube use those cards:

- Damage: Machamp does 20 damage for each Fighting Pokémon in your discard pile. Hisuian Basculegion does 20 damage for each basic Energy card in your discard pile. Kyogre does the same for each Basic Water Energy card. Basculegion and Kyogre then shuffle those Energy cards back into your deck.
- Energy: Flaaffy, Malamar, Bronzong, Mewtwo, Chi-Yu, Volcanion, Arcanine and Cinderace attach Energy from your discard pile.
- Supporters and Trainers: VS Seeker, Cynthia & Caitlin, Lusamine, Dialga and Regieleki put cards from your discard pile into your hand.

A discard deck makes its own deck smaller. Mill decks can win faster against it.

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
| Fire | 39 | Grass 21, Metal 18 |
| Fighting | 38 | Lightning 19, Colorless 13, Darkness 6 |
| Lightning | 31 | Water 16, Colorless 7, Darkness 4, Metal 3, Lightning 1 |
| Water | 23 | Fire 21, Fighting 2 |
| Grass | 17 | Darkness 9, Fighting 7, Water 1 |
| Darkness | 15 | Psychic 15 |
| Psychic | 13 | Fighting 11, Psychic 2 |
| Metal | 6 | Water 4, Psychic 2 |

Fire and Fighting have the widest coverage.
Weakness Policy and Coating Metal Energy are the counters in the cube.

## Watch list

Check these points after the first drafts:

1. **Fire speed.** Stoke, Burn Brightly, Chi-Yu and the 240-damage Arcanine can end games quickly. Five-prize games give slower decks more time.
2. **Weakness coverage.** Fighting and Fire each hit about 40 Pokémon for double damage.
3. **Damage counters on the Bench.** Dusclops, Dusknoir, Obstagoon, Absol, Hawlucha and Risky Ruins can Knock Out small support Pokémon. Risky Ruins puts 2 damage counters on each Basic non-Darkness Pokémon that a player puts onto the Bench. Machoke prevents damage and damage counters on the Bench. Shaymin and Manaphy prevent attack damage to the Bench.
4. **Cofagrigus.** Law of the Underworld puts 6 damage counters on each Pokémon with an Ability, on both sides, for one Energy. Check how often it decides games.
5. **Hex Maniac.** It turns off all Abilities for one turn. The cube has many Ability engines, so this card is strong.
6. **Bench limits.** Sudowoodo and Collapsed Stadium limit each Bench to four Pokémon. Decks with four evolution lines feel this limit more.
7. **Mill speed.** Bunnelby can mill 2 cards each turn, but Super Rod, Miriam, Brock's Grit and other cards shuffle cards back into the deck. Check that milling decks can win.
8. **Time Spiral.** Celebi's devolve attack shuffles the top stage of an evolved Pokémon into the opponent's deck. In a singleton cube, that card is often the only copy. Check that it is not too strong.

## Cards left out

### Over the price limit

These popular cube cards cost more than 10 USD on 2026-10-21:

| Card | Printing | Price (USD) | Replacement in the cube |
|---|---|---|---|
| Ditto ◇ | Lost Thunder 154 | 50.08 | None. The cube has no Ditto. |
| Lapras | Legend Maker 8 | 53.51 | None. The cube has no Lapras. |
| Pidgeot | FireRed and LeafGreen 10 | 17.95 | Team Up Pidgeotto (Air Mail) |
| Shaymin | HeartGold and SoulSilver Unleashed 8 | 15.46 | Destined Rivals Shaymin (Flower Curtain) |
| Azelf | Legends Awakened 19 | 10.88 | Surging Sparks Azelf |
| Jirachi | Team Up 99 | 10.59 | Stellar Crown Jirachi |

Legends Awakened Uxie (43) costs about 18.67 USD.
The cube plays the same card as the 30th Celebration Classic Collection reprint (me55c-43), which costs about 5.48 USD.

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

- Ultra Prism Pachirisu. Its attack needs Benched Pokémon with the Nuzzle attack.
- Shining Legends Pokémon Breeder. It has the same name as the Base Set card, but a different effect. The cube uses the Base Set 2 card.

### Abilities that work only in part

- Twilight Masquerade Thwackey is in the cube. Its Boom Boom Groove Ability works only when your Active Pokémon has the Festival Lead Ability. Prismatic Evolutions Goldeen is the only card in the cube with Festival Lead. A Grass and Water deck can use the two cards together.
- Goldeen's Festival Lead lets it attack two times only when Festival Grounds is in play. Festival Grounds is not in the cube, so this part does nothing.

### Weak in a singleton cube

- Twilight Masquerade Drifblim. Its damage counts Drifloon and Drifblim in play. A singleton cube has only one of each.

## Lost Zone cards

One card uses the Lost Zone: Faba.
It is not a Lost Zone payoff, and the cube has no Lost Zone strategy.

- Faba removes a Tool, Special Energy or Stadium permanently. Cards in the Lost Zone cannot come back, so Lusamine cannot return a Stadium that Faba removes.

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
| 2026-10-21 | Added healing, tank and control support, and cut weak or extra draw cards. Grass: Celebi (swsh45-3) became Unified Minds Celebi (sm11-4, Time Spiral), Exeggcute became Durant (xy9-9), and Destined Rivals Shaymin became Lost Thunder Shaymin (sm8-33, Floral Heal). Fire: Oricorio became Paldea Evolved Oricorio (sv2-33, Ardent Dancing). Lightning: the Blitzle and Zebstrika line became a Toxel (swsh2-68) and Toxtricity (sv3-72) line. Psychic: Dusknoir became Boundaries Crossed Dusknoir (bw7-63, Sinister Hand). Fighting: the Rockruff and Lycanroc line and Regirock became a Nacli, Naclstack and Garganacl line (sv2-121 to sv2-123). Colorless: the Bidoof and Bibarel line became a Chansey and Blissey line (pgo-51, pgo-52), Ditto became Miltank (sm4-78), Lugia became Bunnelby (xy5-121), Oranguru became Sword and Shield Oranguru (swsh1-148, Primate Wisdom), and the Doduo and Dodrio line became the 151 cards (sv3pt5-84, sv3pt5-85). Trainers: Full Heal became Energy Removal (base4-119), Energy Search became Ether (bw8-121), and Penny became Eri (sv5-146). |
| 2026-10-21 | Changed the scripts to show Ancient Traits, such as Bunnelby's Ω Barrage, in the card text. |
| 2026-10-21 | Replaced Shrouded Fable Duskull (sv6pt5-18) with Vivid Voltage Duskull (swsh4-69). Its Future Sight attack rearranges the top 4 cards of either player's deck, which sets up Slowking's Seek Inspiration and Bunnelby's mill. |
| 2026-10-21 | Replaced Paldea Evolved Nacli (sv2-121) with Paradox Rift Nacli (sv4-102). The Garganacl line is now Paradox Rift Nacli, Paldea Evolved Naclstack (sv2-122) and Paldea Evolved Garganacl (sv2-123). |
| 2026-10-21 | Kept Sword and Shield Galarian Obstagoon (swsh1-119, Untamed Shout). The Champion's Path card (Wicked Ruler) is not in the cube. |
| 2026-10-21 | Replaced Pokémon GO Chansey (pgo-51) with 151 Chansey (sv3pt5-113, Lucky Bonus). Pokémon GO Blissey still evolves from it. |
| 2026-10-21 | Replaced 151 Doduo (sv3pt5-84) with BREAKthrough Doduo (xy8-116). Its Doduo Delivery attack draws 2 cards. 151 Dodrio still evolves from it. |
| 2026-10-21 | Replaced Energy Removal with Plumeria (sm3-120). Energy Removal discarded an Energy with no cost, which was too strong. Plumeria costs 2 cards from your hand and your Supporter for the turn. Brought Energy Search (swsh1-161) back and cut Poké Ball (swsh2-164) to make room for it. |
| 2026-10-21 | Replaced Tool Scrapper (swsh2-168) with Trick Shovel (xy2-98). Trick Shovel looks at the top card of either player's deck, then discards it or puts it back. It helps mill decks and Slowking. Field Blower, Lost Vacuum and Faba still remove Tools and Stadiums. |
| 2026-10-21 | Replaced Recycle Energy (sm11-212) with the Risky Ruins Stadium (me1-127). Risky Ruins puts 2 damage counters on each Basic non-Darkness Pokémon that a player puts onto the Bench. It helps Darkness and the damage-counter deck. The cube now has 10 Stadiums and 24 Special Energy cards. |
| 2026-10-22 | Synced the card list with the CubeKoga list, which is the source of truth. Changes: the Sentret and Furret line became a Noibat (sm3-109) and Noivern (sv9-128) line; Doduo is BREAKthrough #115 (xy8-115); Oricorio is Guardians Rising (sm2-14); Shaymin is Destined Rivals (sv10-10); Minun is Supreme Victors (pl3-71) and Plusle is Fusion Strike (swsh8-89); Duskull is Shrouded Fable (sv6pt5-18); Poké Ball, Tool Scrapper and Lysandre (xy2-90) are in; Trick Shovel, Hop and Eri are out. |
| 2026-10-22 | Kept Supreme Victors Minun (pl3-71, about 26 USD) as the one card over the 10 USD limit. It is listed in `price_exceptions` in `cube/page_config.json`, and the page says that one card is over the limit. |
| 2026-10-22 | Synced the card list with the CubeKoga list again. Changes: Thwackey is Twilight Masquerade (sv6-15); the Wimpod and Golisopod line became a Goldeen (sv8pt5-20) and Seaking (me5-14) line; Duskull is Vivid Voltage (swsh4-69) again; Uxie is the 30th Celebration Classic Collection reprint of Legends Awakened Uxie (me55c-43); the Galarian Meowth and Galarian Perrserker line became Archaludon (sv7-107), which evolves from the existing Duraludon; Perfect Order Klefki (me3-59) takes the open Metal Basic slot. |
| 2026-10-22 | Added `price_overrides` to `cube/page_config.json`. The Pokémon TCG API has no TCGplayer price yet for Klefki, Seaking and Uxie. The overrides hold their TCGplayer market prices from 2026-10-22. |
| 2026-10-22 | Synced the card list with the CubeKoga list again. Changes: Battle Compressor (xy4-92) and Brilliant Blender (sv8-164) replaced Poké Ball (swsh2-164) and Lost Vacuum (swsh11-162); Hisuian Basculegion (swsh11-45) evolves from the existing Hisuian Basculin; Mega Evolution Kyogre (me1-34) is in; Lapras (sv3pt5-131) and Suicune (swsh3-37) are out; Toxel is Phantasmal Flames (me2-67). Water now has five Stage 1 lines and five Basics. Brilliant Blender is the only ACE SPEC card in the cube. Faba is now the only Lost Zone card. |
| 2026-10-22 | Phantasmal Flames Toxel is a Darkness Pokémon. It stays in the Lightning section because Lightning Toxtricity evolves from it. Its Call for Family attack needs a Darkness Energy. |
| 2026-10-22 | Synced the card list with the CubeKoga list again. Remoraid is Plasma Blast (bw10-18). Its Bubble Beam attack can Paralyze the Defending Pokémon. Its Weakness is Lightning, not Grass. |

## Options

These changes are possible. They are not in the cube now.

- **Add the 4-prize cards back.** For 5-prize games, add Kartana, Gouging Fire, Lacey or Roxanne.
- **Regi package.** Add Stormfront Regigigas (about 7 USD), Astral Radiance Regice and Astral Radiance Regirock. The two Astral Radiance cards have Regi Gate. Stormfront Regigigas is a weak card, so this package is for fun only.
- **Remove the Lost Zone.** Replace Faba with another removal card.
