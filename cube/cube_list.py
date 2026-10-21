"""The Poké Mart Cube card list. This file is the source of truth.

Every entry is one card. Card IDs are Pokémon TCG API IDs (set id + "-" + number),
for example "sv6pt5-5" is Shrouded Fable 5 (Decidueye).

Rules the build script checks:
  * exactly 360 cards, every card once (singleton)
  * every card name once, and every Pokémon species once
  * every card under the price limit (TCGplayer market, cheapest version)
  * every evolution line is complete inside its group

P holds tuples of (id, count, section, line, note). The section is a type for Pokémon,
or Supporter / Item / Tool / Stadium / Energy. The line groups cards on the page.
The note is a short role summary shown next to the card.
"""
P = []


def add(sec, line, items):
    for it in items:
        P.append((it[0], 1, sec, line, it[1] if len(it) > 1 else ''))

# GRASS
add('Grass','Decidueye',[('sv6pt5-3','Add On: draw 1'),('sv6pt5-4',),('sv6pt5-5','draw to 7 / 170 for G')])
add('Grass','Rillaboom',[('swsh1-11',),('swsh1-12',),('swsh45-13','Voltage Beat: 2 Grass from deck')])
add('Grass','Lurantis',[('sm1-14',),('smp-SM25','Sunny Day: Grass and Fire +20')])
add('Grass','Eldegoss',[('swsh1-20','Call for Family'),('swsh7-16','Cotton Lift: 2 basic Energy')])
add('Grass','Breloom',[('sv5-6',),('sv5-7','120 for GC')])
add('Grass','Yanmega',[('swsh12pt5-8',),('swsh12pt5-9','160 for GGC')])
add('Grass','Basics',[('bw9-4','Propagation'),('sv10-10','Flower Curtain: Bench shield'),('swsh45-3','Woodland Stroll'),('swsh6-19','Pack Call'),('sm8-16','Fresh Squeezed'),('swsh7-6',),('sm8-18',)])
# FIRE
add('Fire','Charizard',[('swsh4-23','Collect'),('sm75-2','Burning Fighter'),('pgo-10','Burn Brightly: basic Fire = FF')])
add('Fire','Cinderace',[('swsh1-31',),('swsh1-32',),('swsh1-34','Libero: reload on switch-in / 190')])
add('Fire','Magcargo',[('sm7-23',),('sm7-24','Smooth Over: tutor to top')])
add('Fire','Arcanine',[('sv1-31','Stoke: 2 Fire from deck'),('sv3pt5-59','reload / 240')])
add('Fire','Salazzle',[('swsh12pt5-27','Call for Family'),('sv7-24','Sudden Scorching: opponent discards up to 3 / 130')])
add('Fire','Rapidash',[('sv5-26',),('sv5-27','120 for FC')])
add('Fire','Basics',[('xy11-25','Power Heater'),('sv8-21','Victory Cheer'),('sm8-48',),('sm12-28',),('sm2-14','Passionate Dance'),('sv4-29','Flare Bringer'),('sv6-30',)])
# WATER
add('Water','Inteleon',[('swsh1-55',),('swsh1-56','Shady Dealings'),('swsh1-58','Shady Dealings x2 / 120+20')])
add('Water','Baxcalibur',[('sv2-58',),('sv2-59',),('sv2-60','Super Cold: attach Water from hand')])
add('Water','Octillery',[('sm4-22',),('xy8-33','Abyssal Hand: draw to 5')])
add('Water','Palafin',[('sv3-60','Valiant Evolution'),('sv3-62','210 after switching in')])
add('Water','Golisopod',[('sm11-50',),('sm11-51','Emergency Exit / First Impression')])
add('Water','Gyarados',[('sv2-42',),('sv2-43','200 for WWCC')])
add('Water','Basics',[('sm2-21','Beacon: search 2 Pokémon'),('sv5-44','Rapid Draw'),('swsh9-41','Wave Veil: Bench shield'),('sv3pt5-131',),('swsh3-37',),('swsh10-43','Gather the Crew'),('sv4-56','Hyper Blower')])
# LIGHTNING
add('Lightning','Ampharos',[('sm8-75','Fluffy Pillow'),('swsh7-55','Dynamotor'),('swsh3-57','130 for LL')])
add('Lightning','Magnezone',[('sm6-34','Searching Magnet'),('sm6-35',),('sm6-36','Magnetic Circuit: attach L from hand')])
add('Lightning','Electrode',[('swsh4-45',),('bw9-33','Magnetic Draw: draw to 4')])
add('Lightning','Raichu',[('sv3pt5-25',),('sv2-64','Electrocharge / 200')])
add('Lightning','Zebstrika',[('sv8-62','Add On'),('sm8-82','Sprint: new hand of 4')])
add('Lightning','Electivire',[('sv7-46',),('sv7-47','220 for LL')])
add('Lightning','Basics',[('sv6-65','190 for LLC'),('smp-SM30','Flying Flip'),('sm35-32',),('sv6-72','Snack Seek'),('swsh10-51',),('sm7-54','Ditch and Draw'),('sm7-53','Draw for Everybody')])
# PSYCHIC
add('Psychic','Gardevoir and Gallade',[('sv4pt5-27',),('swsh12-68','Refinement'),('swsh12-69','Refinement / 120 for PC'),('swsh10-62','Buddy Catch: find a Supporter / 160 for PCC')])
add('Psychic','Dusknoir',[('sv6pt5-18',),('sv8pt5-36','Cursed Blast: 5 counters'),('sv6pt5-20','Cursed Blast: 13 counters / 150')])
add('Psychic','Slowking',[('sv2-85',),('sv7-58','Seek Inspiration / 120')])
add('Psychic','Malamar',[('sm6-50',),('sm6-51','Psychic Recharge')])
add('Psychic','Cofagrigus',[('sv4-75','Ominous Eyes: 3 counters anywhere'),('sv8-83','Law of the Underworld: 6 counters on every Ability Pokémon')])
add('Psychic','Mismagius',[('sm10-77',),('sm10-78','Mysterious Message')])
add('Psychic','Basics',[('cel25-11','Mysterious Tail: find an Item'),('sv8-79','Full Heart: attach 2 P'),('swsh10-65',),('sv8-80',),('dp5-49','QUICK: free-retreat tool'),('swsh12pt5-59','Psypump: reload 2 P / 90, or 180 late')])
# FIGHTING
add('Fighting','Machamp',[('sm2-62',),('sm2-64','Daunting Pose: Bench shield'),('swsh35-26','200 for FFC')])
add('Fighting','Conkeldurr',[('sv6-103',),('sv6-104',),('sv6-105','Tantrum 80 for F / 250')])
add('Fighting','Claydol',[('swsh1-101',),('dp4-15','Cosmic Power: draw to 6')])
add('Fighting','Lucario',[('sv1-113',),('sv1-114','Avenging Knuckle / 120')])
add('Fighting','Donphan',[('swsh4-86',),('cel25c-107_A','Exoskeleton: takes 20 less / Earthquake 60 for F')])
add('Fighting','Lycanroc',[('sv5-89',),('swsh35-30','150 for FFC')])
add('Fighting','Basics',[('sv1-118','Flying Entry'),('sm2-66','Roadblock'),('sv3pt5-106',),('sv3pt5-107','Counterattack'),('swsh4-89',),('sm8-117','Diamond Gate'),('sv5-84','Memory Dive')])
# DARKNESS
add('Darkness','Galarian Obstagoon',[('swsh1-117','Headbutt Tantrum'),('swsh1-118',),('swsh1-119','Untamed Shout')])
add('Darkness','Crobat',[('sv3pt5-41','Revealing Echo'),('swsh5-90','Discreet Draw'),('swsh5-91','Drastic Draw / 100 for CC')])
add('Darkness','Zoroark',[('swsh7-102',),('xy8-91','Stand In / Mind Jack')])
add('Darkness','Weavile',[('sv2-133',),('sv2-134','Assaulting Hunt')])
add('Darkness','Honchkrow',[('sv2-131',),('sv2-132','140 for DCC')])
add('Darkness','Mightyena',[('sm9-86','Howl in the Dark'),('swsh10-96','Wild Tackle 160 for CCC')])
add('Darkness','Basics',[('dp7-48','Impersonate: use any Supporter'),('xy6-40','Cursed Eyes'),('xy11-65','Oblivion Wing'),('sv3-136',),('swsh7-93','Malevolent Charge'),('sm11-140',),('sm10-112','Building Spite')])
# METAL
add('Metal','Metagross',[('swsh4-116','Call for Family'),('sv5-114','Metal Maker'),('sv5-115','Meteor Mash / 200')])
add('Metal','Corviknight',[('sv2-164',),('sv2-165',),('sv2-148','200 for MCC')])
add('Metal','Bronzong',[('sm9-100','Evolutionary Advantage'),('xy4-61','Metal Links')])
add('Metal','Copperajah',[('sv2-149',),('sv6pt5-42','Massive Body / 230')])
add('Metal','Galarian Perrserker',[('swsh1-127',),('swsh1-128','Steely Spirit: Metal +20')])
add('Metal','Scizor',[('sv5-1',),('sm8-126','Exoskeleton')])
add('Metal','Basics',[('sv7-98','Swelling Wish'),('swsh6-114','130 for MMC'),('swsh10-108','Regi Gate'),('sv5-112',),('cel25-20','Temporal Backflow'),('swsh2-138',),('swsh12pt5-97','Metal Shield')])
# COLORLESS
add('Colorless','Pidgeot',[('sm9-121','Collect'),('sm9-123','Air Mail'),('sv3pt5-18','Fly 150')])
add('Colorless','Porygon-Z',[('sm10-155','Quick Draw'),('dp4-49','Download: use a Supporter'),('swsh6-118','Superbeam 170')])
add('Colorless','Bibarel',[('swsh9-120',),('swsh9-121','Industrious Incisors: draw to 5')])
add('Colorless','Cinccino',[('swsh9-124','Call for Family'),('swsh1-147','Make Do')])
add('Colorless','Furret',[('swsh3-135',),('swsh3-136',)])
add('Colorless','Dodrio',[('sm10-150',),('sm10-151',)])
add('Colorless','Basics',[('dp5-55','Mimic'),('swsh4-131','Gormandize'),('sm7-110','Strike and Run'),('sm1-113','Instruct'),('sv3pt5-132',),('sm9-128','Fast Evolution'),('sv1-151','Nest Stash'),('swsh3-140',)])
# SUPPORTERS
add('Supporter','Draw',[('sv8pt5-125',),('sm5-119',),('sv1-176',),('xy10-105',),('sv4pt5-80',),('swsh35-56',),('swsh7-143',),('bw11-109',),('sm1-122',),('sm7-148',),('swsh35-53',),('swsh3-159',),('sm1-128',),('bw8-118',),('sm115-56',),('sv9-149',),('sv2-179',),('swsh7-164',),('sv2-184',),('sv5-147',),('sv4-172',),('sv3-194',),('sv6-145',),('sm12-189',)])
add('Supporter','Search',[('swsh35-65',),('swsh2-166',),('sv1-166',),('sv1-175',),('rsv10pt5-84',),('sm2-127',),('sm8-188',),('sm12-201',),('swsh10-147',),('sm5-135',),('swsh3-165',),('sv8pt5-105',),('sv6-160',),('sv8-174',),('swsh7-152',),('sm7-145',),('xy6-94',)])
add('Supporter','Gust and disruption',[('me1-114',),('sm3-115',),('xy1-129',),('xy7-75',),('sm8-173',)])
add('Supporter','Recovery and healing',[('swsh6-145',),('sm115-53',),('sv6-155',),('sm3-112',),('sm4-95',),('me1-123',),('sm4-96',),('sv1-179',),('sv1-183',)])
add('Supporter','Energy and damage',[('sm3-116',),('swsh1-157',),('swsh4-147',),('swsh4-154',)])
# ITEMS
add('Item','Pokémon search and evolution',[('sv1-191',),('base4-105',),('swsh9-150',),('sv1-181',),('swsh8-237',),('swsh5-129',),('swsh1-164',),('swsh1-163',),('sm9-152',),('sv5-144',),('sm1-134',),('col1-78',),('swsh12-153',),('g1-62',),('swsh8-225',),('swsh2-164',),('xy8-140',),('sv8-175',),('sm7-131',),('dp7-86',),('swsh10-146',),('sm8-187',),('xy5-125',),('swsh6-140',)])
add('Item','Energy search and recursion',[('sv4-163',),('swsh1-161',),('xy1-123',),('sm10-173',),('sm2-119',),('swsh10-139',),('swsh1-170',)])
add('Item','Card search and draw',[('sv1-186',),('xy6-92',),('xy4-109',),('swsh1-172',),('xy5-122',),('swsh12pt5-145',)])
add('Item','Switch and gust',[('swsh12pt5-144',),('swsh5-125',),('swsh10-154',),('sm3-124',),('swsh2-165',),('sv4-160',),('swsh12pt5-138',)])
add('Item','Recovery',[('sv2-188',),('sm2-130',),('bw1-92',),('swsh1-171',),('sv6pt5-61',),('sv2-189',),('xy7-72',),('xy12-85',)])
add('Item','Utility',[('swsh12pt5-129',),('swsh1-159',),('sv6-148',),('sm2-125',),('swsh2-168',),('swsh11-162',),('xy9-103',),('swsh1-166',),('xy12-87',),('swsh35-51',)])
# TOOLS
add('Tool','Tools',[('xy8-137',),('zsv10pt5-79',),('sm5-122',),('sv8pt5-126',),('sm1-118',),('xy1-121',),('swsh1-185',),('sv1-169',),('swsh4-159',),('sv2-173',),('swsh1-158',),('sv8-169',),('sm3-126',),('sv3pt5-163',),('sv6-158',)])
# STADIUMS
add('Stadium','Stadiums',[('sm9-156',),('swsh2-169',),('sv4pt5-76',),('sv1-178',),('sv1-167',),('swsh10-148',),('xy6-89',),('sv3-196',),('swsh9-137',)])
# SPECIAL ENERGY
add('Energy','Special Energy',[('xy12-90',),('swsh2-174',),('sm1-137',),('swsh1-186',),('sv2-191',),('zsv10pt5-86',),('ex2-93',),('sm4-100',),('sv2-192',),('swsh2-171',),('sv2-190',),('sm11-212',),('swsh11-171',),('sm5-137',),('sm5-138',),('sm6-118',),('bw6-117',),('swsh4-162',),('swsh3-174',),('swsh4-165',),('swsh2-173',),('swsh2-172',),('swsh4-164',),('swsh3-175',),('swsh4-163',)])
