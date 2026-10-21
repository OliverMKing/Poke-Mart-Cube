# (id, count, section, group/line, role note)
P=[]
def add(sec,line,items):
    for it in items: P.append((it[0],it[1],sec,line,it[2] if len(it)>2 else ''))
# ---------- GRASS ----------
add('Grass','Decidueye (Stage 2)',[('sv6pt5-3',4,'Add On: draw 1'),('sv6pt5-4',3),('sv6pt5-5',2,'draw to 7 / 170 for G')])
add('Grass','Lurantis (Stage 1)',[('sm1-14',3),('smp-SM25',1,'Sunny Day: Grass+Fire +20'),('sv10-14',1,'130 for G, discard 2 basic G')])
add('Grass','Eldegoss (Stage 1)',[('swsh1-20',3,'Call for Family'),('swsh7-16',2,'Cotton Lift: 2 basic Energy/turn')])
add('Grass','Basics',[('bw9-4',1,'Propagation: discard-pile recursion'),('sv10-10',1,'Flower Curtain: Bench protection')])
# ---------- FIRE ----------
add('Fire','Charizard (Stage 2)',[('sv4pt5-7',2),('swsh4-23',2),('sv4pt5-8',2,'Flare Veil'),('sm75-2',1,'Burning Fighter: mill-accelerate'),('pgo-10',2,'Burn Brightly: basic Fire = FF')])
add('Fire','Magcargo (Stage 1)',[('sm7-23',3),('sm7-24',2,'Smooth Over: tutor to top')])
add('Fire','Arcanine (Stage 1)',[('sv1-31',3,'Stoke: 2 Fire from deck'),('sv3pt5-59',1,'240 / reload from discard'),('xy12-18',1,'Burning Road')])
add('Fire','Basics',[('xy11-25',1,'Power Heater: accel from discard'),('sv8-21',1,'Victory Cheer +10')])
# ---------- WATER ----------
add('Water','Inteleon (Stage 2)',[('swsh1-55',2),('swsh1-54',2),('swsh1-56',3,'Shady Dealings: tutor 1 Trainer'),('swsh1-58',2,'Shady Dealings x2 / 120+20 snipe')])
add('Water','Octillery (Stage 1)',[('sm4-22',3),('xy8-33',2,'Abyssal Hand: draw to 5')])
add('Water','Palafin (Stage 1)',[('sv3-60',3,'Valiant Evolution'),('sv3-62',2,'210 for WW after switching in')])
add('Water','Basics',[('sm2-21',1,'Beacon: search 2 Pokemon'),('sv5-44',1,'Rapid Draw / 110')])
# ---------- LIGHTNING ----------
add('Lightning','Ampharos (Stage 2)',[('sm8-75',1,'Fluffy Pillow'),('swsh7-54',3),('swsh7-55',3,'Dynamotor'),('swsh3-57',2,'130 for LL')])
add('Lightning','Electrode (Stage 1)',[('swsh4-45',3),('bw9-33',1,'Magnetic Draw: draw to 4'),('swsh4-46',1,'Buzzap Generator')])
add('Lightning','Raichu (Stage 1)',[('sv3pt5-25',2),('swsh7-49',1),('sv2-64',1,'Electrocharge / 200'),('sm3-41',1,'Evoshock paralysis')])
add('Lightning','Basics',[('sv6-65',1,'190 for LLC'),('smp-SM30',1,'Flying Flip spread')])
# ---------- PSYCHIC ----------
add('Psychic','Gardevoir (Stage 2)',[('sv4pt5-27',2),('swsh12-67',2),('swsh12-68',3,'Refinement'),('swsh12-69',2,'Refinement / 120 for PC')])
add('Psychic','Dusclops (Stage 1)',[('sv6pt5-18',3),('sv8pt5-36',2,'Cursed Blast: 5 counters')])
add('Psychic','Slowking (Stage 1)',[('sv2-85',3),('sv7-58',2,'Seek Inspiration / 120')])
add('Psychic','Basics',[('cel25-11',1,'Mysterious Tail: find Item'),('sv8-79',1,'Full Heart: attach 2 P')])
# ---------- FIGHTING ----------
add('Fighting','Machamp (Stage 2)',[('sm2-62',2),('sv3pt5-66',2),('sm2-64',3,'Daunting Pose: Bench shield'),('sv3pt5-68',1,'Guts / 100 for FF'),('swsh35-26',1,'200 for FFC')])
add('Fighting','Claydol (Stage 1)',[('swsh1-101',3),('dp4-15',2,'Cosmic Power: draw to 6')])
add('Fighting','Lucario (Stage 1)',[('sv1-113',3),('sv1-114',1,'Avenging Knuckle / 120'),('swsh9-79',1,'Roaring Resolve')])
add('Fighting','Basics',[('sv1-118',1,'Flying Entry'),('sm2-66',1,'Roadblock: opp Bench max 4')])
# ---------- DARKNESS ----------
add('Darkness','Galarian Obstagoon (Stage 2)',[('swsh1-117',4,'Headbutt Tantrum'),('swsh1-118',3),('swsh1-119',1,'Untamed Shout'),('swsh35-37',1,'Wicked Ruler / 180')])
add('Darkness','Zoroark (Stage 1)',[('swsh7-102',3),('xy8-91',1,'Stand In / Mind Jack'),('swsh7-103',1,'Phantom Transformation')])
add('Darkness','Weavile (Stage 1)',[('sv2-133',3),('sv2-134',1,'Assaulting Hunt'),('sm5-74',1,'Evil Admonition')])
add('Darkness','Basics',[('dp7-48',1,'Impersonate: any Supporter'),('xy6-40',1,'Cursed Eyes')])
# ---------- METAL ----------
add('Metal','Metagross (Stage 2)',[('sv5-113',2),('swsh4-116',2,'Call for Family'),('sv5-114',3,'Metal Maker accel'),('sv5-115',2,'Meteor Mash / 200')])
add('Metal','Bronzong (Stage 1)',[('sm9-100',3,'Evolutionary Advantage'),('xy4-61',2,'Metal Links accel')])
add('Metal','Copperajah (Stage 1)',[('sv2-149',3),('swsh1-137',1,'220 for MMM'),('sv6pt5-42',1,'Massive Body / 230')])
add('Metal','Basics',[('sv7-98',1,'Swelling Wish'),('swsh6-114',1,'130 for MMC')])
# ---------- COLORLESS ----------
add('Colorless','Pidgeot (Stage 2)',[('sm9-121',2,'Collect'),('sv3pt5-16',2,'Call for Family'),('sm9-123',3,'Air Mail'),('sv3pt5-18',1,'Fly 150'),('sm9-124',1,'Spin Storm bounce')])
add('Colorless','Bibarel (Stage 1)',[('swsh9-120',3),('swsh9-121',2,'Industrious Incisors: draw to 5')])
add('Colorless','Porygon2 (Stage 1)',[('sm10-155',3),('dp4-49',2,'Download: discard Supporter, use it')])
add('Colorless','Basics',[('dp5-55',1,'Mimic'),('swsh4-131',1,'Gormandize'),('sm7-110',1,'Strike and Run')])
# ---------- SUPPORTERS ----------
add('Supporter','Draw',[('sv8pt5-125',4,"Professor's Research"),('sm5-119',3,'Cynthia'),('sv1-176',2,'Judge'),('xy10-105',1,'N'),('sv4pt5-80',2,'Iono'),('swsh35-56',2,'Marnie'),('swsh7-143',2,'Copycat'),('bw11-109',1,'Bianca'),('sm1-122',2,'Lillie'),('g1-72',1,'Shauna'),('sm7-148',2,'Tate & Liza'),('swsh35-53',1,'Hop'),('sm7-132',1,'Hau'),('xy4-107',1,'Tierno'),('bw2-91',1,'Cheren'),('swsh3-159',3,'Bird Keeper'),('sm1-128',1,'Professor Kukui'),('bw8-118',1,'Colress'),('sm115-56',1,"Erika's Hospitality")])
add('Supporter','Search',[('swsh35-65',2,'Sonia'),('swsh2-166',1,'Skyla'),('sv1-166',2,'Arven'),('sv1-175',2,'Jacq'),('rsv10pt5-84',2,'Hilda'),('sm2-127',1,'Mallow'),('sm8-188',1,"Professor Elm's Lecture"),('swsh10-147',1,'Irida'),('sm5-135',1,'Volkner'),('swsh7-152',1,'Raihan')])
add('Supporter','Gust and recovery',[('me1-114',3,"Boss's Orders"),('xy7-78',1,'Lysandre'),('sm3-115',1,'Guzma'),('swsh6-145',1,'Klara'),('sm115-53',1,"Brock's Grit")])
# ---------- ITEMS ----------
add('Item','Pokemon search',[('sv1-191',5,'Rare Candy'),('swsh9-150',4,'Ultra Ball'),('sv1-181',4,'Nest Ball'),('swsh8-237',3,'Quick Ball'),('swsh5-129',3,'Level Ball'),('swsh1-164',3,'Great Ball'),('swsh1-163',3,'Evolution Incense'),('sm9-152',3,'Pokemon Communication'),('sv5-144',2,'Buddy-Buddy Poffin'),('sm1-134',1,'Timer Ball'),('col1-78',1,'Dual Ball'),('swsh12-153',1,'Capturing Aroma'),('g1-62',1,'Evosoda'),('swsh8-225',1,'Battle VIP Pass')])
add('Item','Energy and Supporter search',[('sv4-163',3,'Earthen Vessel'),('swsh1-161',2,'Energy Search'),('xy1-123',1,"Professor's Letter"),('sv1-186',3,'Pokegear 3.0'),('xy6-92',2,"Trainers' Mail"),('xy4-109',1,'VS Seeker'),('swsh1-172',2,'Pal Pad')])
add('Item','Switch and gust',[('swsh12pt5-144',5,'Switch'),('swsh5-125',3,'Escape Rope'),('swsh10-154',2,'Switch Cart'),('sv4-160',3,'Counter Catcher'),('swsh12pt5-138',1,'Pokemon Catcher')])
add('Item','Recovery',[('sv2-188',3,'Super Rod'),('sm2-130',2,'Rescue Stretcher'),('bw1-92',3,'Energy Retrieval'),('swsh1-171',1,'Ordinary Rod'),('sv6pt5-61',2,'Night Stretcher')])
add('Item','Utility',[('swsh12pt5-129',1,'Energy Switch'),('swsh1-159',1,'Crushing Hammer'),('sv6-148',1,'Enhanced Hammer'),('sm2-125',1,'Field Blower'),('xy9-103',1,'Max Potion'),('xy12-87',1,'Super Potion')])
# ---------- TOOLS ----------
add('Tool','Tools',[('xy8-137',1,'Float Stone'),('zsv10pt5-79',1,'Air Balloon'),('sm5-122',1,'Escape Board'),('sm1-118',1,'Exp. Share'),('xy1-121',1,'Muscle Band'),('swsh1-185',1,'Vitality Band'),('sv1-169',1,'Defiance Band'),('swsh4-159',1,'Rocky Helmet'),('sv2-173',1,'Bravery Charm'),('sv8-169',1,'Counter Gain'),('sm3-126',1,'Weakness Policy')])
# ---------- STADIUMS ----------
add('Stadium','Stadiums',[('sm9-156',1,'Viridian Forest'),('swsh2-169',1,'Training Court'),('sv4pt5-76',1,'Artazon'),('sv1-178',1,'Mesagoza'),('sv1-167',1,'Beach Court'),('swsh10-148',1,'Jubilife Village')])
# ---------- SPECIAL ENERGY ----------
add('Energy','Special Energy',[('xy12-90',2,'Double Colorless'),('swsh2-174',1,'Twin'),('sm1-137',2,'Rainbow'),('swsh1-186',1,'Aurora'),('sv2-191',1,'Luminous'),('swsh2-171',1,'Capture'),('sm4-100',1,'Counter'),('sv2-192',1,'Reversal'),('sv2-190',1,'Jet'),('swsh4-162',1,'Aromatic Grass'),('swsh3-174',1,'Heat Fire'),('swsh4-165',1,'Wash Water'),('swsh2-173',1,'Speed Lightning'),('swsh2-172',1,'Horror Psychic'),('swsh4-164',1,'Stone Fighting'),('swsh3-175',1,'Hiding Darkness'),('swsh4-163',2,'Coating Metal')])
