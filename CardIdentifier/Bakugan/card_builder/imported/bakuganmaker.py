""" Bakugan Finder by VioletCat39 """

import csv

# Strings are pulled from text files
# Variables that act as string representations for each attribute
PYRUS1 = "Pyrus:\nPyrus, or Nova in the Japanese version, is the attribute of fire.\nPyrus can be found at the inner core of the universe and is inhabited by Bakugan who draw their strength from the blazing heat that surrounds them. \nIt is within these deep recesses of molten rock that their intensity is forged.\nNever one to waste even a second, the Pyrus blitz their enemies from every angle like a raging firestorm.\n\nFor Pyrus Bakugan, the main point of them is to simply overpower through sheer force and shutting down ways your opponent can fight back like gate card bonuses or Ability Cards.\nDue to this, nullifying cards like Rikimaro's Surprise or Stand Off are very useful to stop your opponent from fighting back with ability cards or Gate effects and Stand Off also gives a great Pyrus Bonus."
PYRUS2 = "Pyrus:\nPyrus is the most aggressive Faction, whose members aim to take out opponents before they even have a chance to get their strategy going.\nPyrus wants to end the game quickly and victoriously!\nIt is the Faction of fire.\nThe region on Vestroia where Pyrus Bakugan reside is known as Pyrule.\n\nThe English name, Pyrus, comes from the Ancient Greek πῦρ.\nThe Japanese name, Nova, stems from the English term nova, which is an astrological event that creates a bright explosion."
PYRUS3 = "Pyrus:\nThe attribute of fire, with great power that can dominate over opponents and greater potential for critical ko!\nThis attribute is good for new players, with any easy strategy to play with.\n\nAttack and Balance are usually Pyrus and Darkus BakuTech that has a special feature that allows it to easily perform Critical K.O. on opponents (Attack).\nWhile some of them have balanced stats in the Pentagon Parameter (Balance)."

AQUOS1 = "Aquos:\nAquos, Aqua in the Japanese version, is the Attribute of water. \nAquos Bakugan usually have average G-Power but use trickery to either boost them or dwindle their opponent to win.\nMany cards make the opponent feel safe and secure but then cards with powerful effects come up and shock the opponent like Preyas Switch, Aquos 1 and Aquos 2, Summon Wave, Marucho's Throw and Marucho's Launcher.\nWith an Aquos strategy, you would want to roll a low power Bakugan on to an opponent's Gate Card or something to make the opponent think they have the upper hand before you bring down a big Ability Card to knock some sense into them and take out their Bakugan!\n\nBoth the English and the Japanese names are derived from the Latin word for water, aqua."
AQUOS2 = "Aquos:\nAquos is the Faction of water.\nThe region on Vestroia where Aquos Bakugan reside is known as Aquilia.\nThese Bakugan are blue, like the powerful water attacks and element they use.\nThis faction has many tricks up its sleeve, and known for its diverse set of abilities and powers."
AQUOS3 = "Aquos:\nThe attribute of water, with sneaky abilities that make for a versatile and fun play style.\nThis attribute is best suited for players with a medium to master knowledge of the game.\n\nTechnique and Trick are usually Ventus and Aquos BakuTech whose special features allow it to:\nEvade Critical K.O. (Trick)\nOr jump/move into another Gate Card (Technique)."

SUBTERRA1 = "Subterra:\nSubterra, also known as Sub Terra, is the Attribute of Earth and Dust.\nSubterra Bakugan have the most Strength and Life, but lack in Agility and Will.\nLike Pyrus, these Bakugan also focus heavily on building up high G-Power for an easy victory,\nSubterra works well with any of the light-side attributes\n\nThe name comes from the word 'subterranean', itself formed from the Latin sub- (meaning under) and terra (meaning earth)."
SUBTERRA2 = "Subterra:\nThe attribute of earth, with a play style centered around gaining high levels of G-power and supporting other Bakugan.\nThese Bakugan work well for any skills level, although medium skills level will be able to use them best.\nThey are also very good as a supporting Bakugan Attribute, especially with the light triad (Pyrus, Aquos, and Haos).\n\nDefense and Occupied are usually Haos and Subterra BakuTech whose special features involve prevention of Critical K.O. (Defense).\nThese types of BakuTech are also characterized by the huge space they occupy on the Gate Card (Occupied)."
AURELUS = "Aurelus:\nAurelus is a mysterious, elusive Faction characterized by raw, golden energy.\nThe region on Vestroia where Aurelus Bakugan reside is known as Aureopolis.\nUnlike all other Factions, Aurelus doesn't represent some element, instead having powerful Bakugan with their own unique abilities.\n\nAurelus Bakugan are known as the 'Golden Ones', with a gold color scheme that represents their noble powers.\nThese Bakugan are protectors of the other Bakugan, and take on the Subterra Attribute in Battle."

HAOS1 = "Haos:\nHaos, Lumina/Rumina in the Japanese version, is the Attribute of Light.\n\nHaos Bakugan have the lowest G-Powers in the game but strategy and manipulation is the main idea.\nHaos Bakugan are often in the battle for aid, or switch.\nThey often use abilities such as G-Power Swap and are often credited with winning the battle with the lowest G-Power.\nHaos Bakugan use very strong Ability Cards such as Haos 2, The Glow, Sagitarius Arrow, Freezing Haos, and Runo's Launcher. "
HAOS2 = "Haos:\nHaos is the Faction of light.\nThe region on Vestroia where Haos Bakugan reside is known as Haora.\n\nThe English name, Haos, is derived from the Ancient Greek ἅλως (hálōs), which has a possible meaning of 'ring of light around the sun or moon.'\nAnother definition of ἅλως is 'disk of a shield.'"
HAOS3 = "Haos:\nThe attribute of light, with abilities and powers that can turn a losing match into a victory with ease.\nThis attribute is best used by high level players, with advanced concepts like rule manipulation that are harder for newer players to master.\nThis attribute has the greatest battle potential if used right, and the worst battle potential if something goes wrong.\n\nDefense and Occupied are usually Haos and Subterra BakuTech whose special features involve prevention of Critical K.O. (Defense).\nThese types of BakuTech are also characterized by the huge space they occupy on the Gate Card (Occupied)."

DARKUS1 = "Darkus:\nDarkus, Japanese Version: Darkon, is the Attribute of Darkness and Tone.\nDarkus Bakugan have a large variety of G-Powers and Ability Cards so there are many ways to use them.\nThey are known for being deceptive Bakugan, with powerful abilities used for treachery combined with the powerful Pyrus strategy."
DARKUS2 = "Darkus:\nDarkus refers to elemental power of shadow and dark energy.\nThe region on Vestroia where Darkus Bakugan reside is known as Darkavia.\n\nThe root word for this attribute in both English and Japanese is the English word dark, which itself is derived from the Proto-Germanic word derkaz.\nNotably, this is the only attribute whose name is derived from an English word."
DARKUS3 = "Darkus:\nThe attribute of darkness, with manipulative and sneaky abilities, with high g power.\nThis attribute is good for players with varying skill level, with a Pyrus strategy combined with special abilities that take time to master.\n\nAttack and Balance are usually Pyrus and Darkus BakuTech that has a special feature that allows it to easily perform Critical K.O. on opponents (Attack).\nWhile some of them have balanced stats in the Pentagon Parameter (Balance)."

VENTUS1 = "Ventus:\nVentus, Zephyros in the Japanese version, is the Attribute of wind.\nThe planet of Ventus is swift and silent yet within its borders lurks a vicious cycle that overwhelms intruders and punishes them for trespassing.\nVentus Bakugan are fast and powerful like hurricane winds.\nOnce their enemies are caught in the eye of the storm, they are defenseless against the Ventus' wrath.\n\nVentus-attributed Bakugan have average G-Power, drawing their power from cunning tactics.\nThey choose their Ability Cards wisely, as the biggest boost is not always the best.\nThey lure their opponent in by giving them the upper hand - then, just when their opponent is getting cocky, they spring their trap and come out victorious!\nWith Ventus-Attributed abilities such as Blow Away, Ventus Bakugan can turn the tides in any battle."
VENTUS2 = "Ventus:\nIt is the Faction of Earth and Wind, although it could be better categorized as the Faction of Nature.\nThe region on Vestroia where Ventus Bakugan reside is known as Ventana.\n\nVentus was developed later than the other five Attributes (debuting at the same time as the Bakugan Battle Brawlers anime in Japan), so Ventus was not included in earlier Japanese/Korean Gate Cards.\nVentus comes from the Latin ventus, which means 'a wind.' \nThe Japanese name, Zephyros, comes from the Greek Ζέφυρος, 'the west wind.'"
VENTUS3 = "Ventus:\nThe attribute of wind and stealth, these Bakugan are known for the element of surprise.\nThis attribute is best suited for high level players with advanced skills and techniques.\n\nTechnique and Trick are usually Ventus and Aquos BakuTech whose special features allow it to:\nEvade Critical K.O. (Trick)\nOr jump/move into another Gate Card (Technique)."

CLEAR_ATTRIBUTE = "Clear:\nThese rare Bakugan have no attribute, and are see-through.\nDuring battle, they take on the opponent Bakugan's attribute, a skill that can be a benefit or a detriment."
DIAMOND1 = "Diamond:\nDiamond Bakugan are clear Bakugan that take on the attribute of the opponent in battle.\nThese Bakugan are incredibly rare to find, and often must be evolved from a base Bakugan."
DIAMOND2 = "Diamond:\nThe Attribute of jewels and crystals, and attribute of rarity and secrets.\nWe don't know much about this attribute."
GALAXY = "Galaxy:\nOne of the rarest Attributes, with the power to take on any attribute of the user's choosing."
ALLFACTION = "Genesis:\nThe Genesis Bakugan are unique Bakugan that possess the power of all 6 Attributes!\nUsing a die or a colored wheel, they shine with the attribute they will take on during battle!\n1 or Red is Pyrus\n2 or Dark Blue is Aquos\n3 or Yellow is Subterra\n4 or Light Blue is Haos\n5 or Purple is Darkus\n6 or Green is Ventus"
NOATTRIBUTE = "NULL ATTRIBUTE:\nThese Bakugan, during the great divide, were separated from the other Bakugan for having no Attribute.\nNow they lurk in the background, waiting for the right time to strike again.\n\nDuring battle, these Bakugan take on the highlighted gate attribute bonus."
# Variables that hold each special color rule
CLEAR_RULE = "Clear Bakugan:\nDuring Battle, clear Bakugan take on the attribute of their opponent's Bakugan in the battle.\n If two clear bakugan are in a battle, both players can choose their Bakugan's attribute before the gate card is revealled."
TRANSLUCENT = "Translucent Bakugan:\nDuring Battle, Translucent Bakugan can take on the Attribute of their opponent's Bakugan or take on their printed attribute."
DUAL_ATTRIBUTE = "Dual Attribute Bakugan:\nThese Bakugan can choose one of the two Attributes printed on them to play as during battle."
PEARL = "Pearl bakugan:\nThese Bakugan can choose to take the highlighted G-power bonus on their gate card, or the G Power bonus of their attribute."
FLIP = "BakuFlip\n:These Bakugan have a reverse color scheme."
BAKUCORE = "BakuCore:\nThese Bakugan have a 'Battled Damaged' addition to their color scheme."
BRONZE = ""
BRONZE_ATTACK = ""
FROST = ""
STEEL = ""
BAKUMUTATION = ""
SOLAR = "BakuSolar:\nThese Bakugan are bright orange and translucent.\nDuring Battle, Translucent Bakugan can take on the Attribute of their opponent's Bakugan or take on their printed attribute."
BAKUBLUE = "BakuBlue:\nThese bright, light blue or torquoise Bakugan can the Attribute printed on them, or the highlighted gate attribute bonus."
BAKUCAMO = "BakuCamo:\nThese Bakugan have a camoflauged texture printed upon them.\nThey are treated as BakuCore Bakugan."
EXOSKIN = "EXO Skin:\n These Bakugan have a special texture, or lack of texture, on their closed ball form."
BAKUGRANITE = ""
BAKUMETALIX = "BakuMetalix:\nThese Bakugan have metal parts on their bodies."
BAKUSHADOW = ""
BAKUSTAND = "BakuStand:\nThese Bakugan stand tall above their opponents."
CRIMSONPEARL = "Crimson and Pearl: These Bakugan can take their attribute's Gate Attribute Bonus, or the Highlighted Gate Attribute Bonus."
EVILTWIN = "Evil Twin:\nThese Bakugan are evil clones of their original Bakugan."
# Variables that hold each special attack rule
HEAVY_METAL = "Heavy Metal Bakugan:\nThese Bakugan have metal parts and/or bands designed for extra stability and critical ko potential."
SPIN = "Spin Bakugan:\nThese Bakugan spin open when they land on a gate card."
ATTRIBUTE_DICE = "AttributeDice:\nThis Bakugan can change attribute based on the roll of a die."
GPOWER_DICE = "G-Power Dice:\nThis Bakugan changes G-Power based on the roll of a die or wheel within it."
JUMPING = "Jumping Bakugan:\nThis Bakugan, rolled correctly on a hard surface, can jump over opponent Bakugan."
RIPCORD = "Ripcord Bakugan:\nThese Bakugan have a ripcord slot that allows them to spin into battle at high speeds."
LIGHTUP = "Light Up Bakugan:\nThese Bakugan light up when they open up on a gate card."
BAKUTREMOR = "BakuTremor Bakugan:\nThese Bakugan shake the gate card when they open up."
BAKUVICE = "BakuVice Bakugan:\nThese Bakugan extend open, making potential for a Critical KO."
DOUBLE_MAGNET = "Double Magnet Bakugan:\nThese Bakugan have two magnets, with double the potential for opening."
DOUBLE_STRIKE = "Double Strike Bakugan:\nThese Bakugan has a special button that may be activated to give them an additional G-power bonues on an enemy's gate card."
SKY_GAIA_ATTACK = "Sky and Gaia Dragonoid:\nThis Bakugan has a special rule by Spin Master:\n'How do I use Sky and Gaia Dragonoid in battle?\nRoll Sky and Gaia Dragonoid into battle.\nIf both halves of the Bakugan land on separate Gate Cards they are treated just like two separate Bakugan on two different Gate Cards.\nIf you get both halves to land on the same Gate Card, you have to decide which Bakugan will move to the other Gate Card in play.\nIf that starts two battles, the player who rolled Sky and Gaia Dragonoid gets to pick which battle to do first.\nIf both halves land on the same Gate Card (and it's the last Gate Card in play) you have to decide which one will be used for battle and which one will be put into your Used pile.\nIf one half lands on a card and the other half lands elsewhere, then the top half goes to the Used pile, and it cannot be rolled again until the bottom half also goes to the Used pile at which time they move as a pair to the unused pile.'"
SKY_RAIDERS_ATTACK = "Sky Raiders:\nThese Bakugan jump into the air after standing.\nIf they land on another gate card after jumping, you may choose which card the Bakugan stands on."

# Variables that hold special rules for the Bakugan
SKY_GAIA_RULES = "\nSky and Gaia Dragonoid:\nThis Bakugan has a special rule by Spin Master:\n'How do I use Sky and Gaia Dragonoid in battle?\nRoll Sky and Gaia Dragonoid into battle.\nIf both halves of the Bakugan land on separate Gate Cards they are treated just like two separate Bakugan on two different Gate Cards.\nIf you get both halves to land on the same Gate Card, you have to decide which Bakugan will move to the other Gate Card in play.\nIf that starts two battles, the player who rolled Sky and Gaia Dragonoid gets to pick which battle to do first.\nIf both halves land on the same Gate Card (and it's the last Gate Card in play) you have to decide which one will be used for battle and which one will be put into your Used pile.\nIf one half lands on a card and the other half lands elsewhere, then the top half goes to the Used pile, and it cannot be rolled again until the bottom half also goes to the Used pile at which time they move as a pair to the unused pile.'"
SKY_RAIDERS_RULES = "\nSky Raiders Abiltiy Mechanic:\nBefore rolling your Bakugan Sky Raiders,\nOnce per game, you may place down an ability or a refernce card onto the field from your unused pile.\nWhen your Sky Raiders Bakugan opens on a gatecard, if it flips open and lands on the card, you may play the card now or later in a battle with the Sky Raiders Bakugan for free, and may replace it into your unused pile when you are done.\nIf you miss the card, the ability or reference card goes back into your unused pile.\n\nBaku-Snap Mechanic:\nIf this Bakugan has a Baku-snap additional G-Power Boost,\nAdd G-power from both 'snaps' to your Bakugan during Battle."
EVOLUTION_RULE = "\nEvolutions:\n(Marked as 'EV')\nPlay before you roll and have a standing a Bakugan of the same attribute or type on a gate card.\nIf this evolution is in your unused pile, you may replace the Bakugan stood on the gate card with this Bakugan.\nPut the old Bakugan into this pile, and put the evolution in your used pile after battle.\nThis Bakugan goes through the regular used and unused pile cycle with other Bakugan, and counts as one of the three (or six in the big game) Bakugan you are allowed.\nYou may play any text on the back of this Bakugan's card."
SUPER_EVOLUTION_RULES = "\nSuper Evolutions!\n(Marked as Special EVO, or has separate character card)\nPlay before you roll a compatible Bakugan onto a gate card (inidcated by Card Text).\nYou may play an abilities ont he back of the card once per game.\nYou may roll the evolved Bakugan instead (either by playing the evo card, or rolling the Super Evolutions Bakugan).\nThe Bakugan remains evolved until it has been in a battle (if using a physical evolution, the evolved Bakugan ball replaces the unevolved form).\nWhen the battle is over, the Bakugan is 'un-evolved,' and the evolution card or form goes into the used pile with the un-evolved Bakugan.\nUnlike other Bakugan, super evolutions do not cycle back into your unused pile once they have battled.\nYou may not use a super evolution more than once per game, unless card rules specify otherwise."
BATTLE_GEAR_COMPATIBLE = "\nBattle Gear Compatibility Mechanic:\nIf this Bakugan is Battle Gear Compatible,\nYou may play a Battle Gear from your unused pile on this Bakugan during battle.\nBattle Gear goes into your used pile after battle.\nBattle Gear cycles back to the unused pile with the Bakugan."
BAKU_GEAR_COMPATIBLE = "\nBaku Gear Compatibility Mechanic:\nIf this Bakugan is a Baku Gear Compatible Bakugan Ultra, \nYou may play the Bakugan's corresponding Bakugear from your unused pile during Battle.\nWhen the battle is over, the Bakugear goes into your used pile.\nBakugear does not cycle back to your unused pile with your Bakugan."
NANO_COMPATIBLE = "\nBaku Nano Compatibility Mechanic:\nIf this Bakugan is BakuNano or Nanogan compatible,\nYou may play a Bakunano or Nanogan from your unused pile with this Bakugan.\nAfter the battle, the Nanogan or BakuNano goes into you used pile, and it does not cycle back to your unused pile with your Bakugan."
BAKUMUTANT_RULES = "\nBakuMutant Mechanic:\nThis Bakugan is considered Dual Attribute.\nDuring Battle, you may add one of the G-Power bonuses from the inside of the Bakugan to this Bakugan.\nOnce per Game, during battle,\nIf this Bakugan has the lowest printed G-power and it is on an enemy's gate card,\nAdd the second G-power bonus."
BAKUBIND_RULES = "\nBakuBind Mechanic:\nIf two of your BakuBind Bakugan land on the same gate card,\nYou may Swap Bases, the top half containing the name of the Bakugan, the botton half containing the G-power of the Bakugan.\nIf the two halves are different attributes, the Bakugan is considered Dual Attribute.\nMove one of these BakuBind Bakugan to your used pile, and leave the other on the gate card.\nThese Bakugan cannot perform Double Stand."
SYNCHRO_BAKUGAN_RULES = "\nSynchro Bakugan Mechanic:\nA Synchro Bakugan must be summoned through regular evolution mechanics.\nIf the Synchro Bakugan stands on the gate card through a normal role, it may not be played as a Synchro Bakugan, and is subject to normal Bakugan Treatment.\nThis Bakugan can be combined with another Bakugan, without regards to G-power (see: Combo Mechanic).\nYou may play any abilities on the back of this Bakugan's Card.\n\nEvolutions:\nPlay before you roll and have a standing Bakugan with the same attribute or type on a gate card. \nIf this evolution is in your unused pile, you may replace the Bakugan stood on the gate card with this Bakugan.\nPut the old Bakugan into this pile, and put the evolution in your used pile after battle.\nThis Bakugan goes through the regular used and unused pile cycle with other Bakugan, and counts as one of the three (or six in the big game) Bakugan you are allowed. \n\nCombo Mechanic:\nOnce per game,\nIf two combinable Bakugan land on the same Gate Card, and one is less than 500 G power, \nYou may combine these two Bakugan, adding both of their G-Powers together.\nIt can be considered dual attribute if the two attributes of the Bakugan are different.\nThis combination lasts until the battle with this combination is finished.\nAfter Battle, these Bakugan unfuse and are placed in your used pile."
BAKUFUSION_RULES = "\nBakuFusion Mechanic:\nThis Bakugan is considered Dual Attribute, and has the names/types of both Bakugan listed on the card.\n\nOnce per game, you may 'fuse' this Bakugan during battle.\nIf you do so, turn the Bakugan's character card over, and play using the new G-Power.\nYour Bakugan also gets both Gate Attribute Bonuses, and is considered to have both Attributes for the rest of the battle, taking in any bonuses for both attributes and triggering any effects. \n\nBaku Gear Compatibility Mechanic:\nIf this Bakugan is a Baku Gear Compatible Bakugan Ultra, \nYou may play the Bakugan's corresponding Bakugear from your unused pile during Battle.\nWhen the battle is over, the Bakugear goes into your used pile.\nBakugear does not cycle back to your unused pile with your Bakugan.\n\nBaku Nano Compatibility Mechanic:\nIf this Bakugan is BakuNano or Nanogan compatible,\nYou may play a Bakunano or Nanogan from your unused pile with this Bakugan.\nAfter the battle, the Nanogan or BakuNano goes into you used pile, and it does not cycle back to your unused pile with your Bakugan."
COMBO_MECHANIC = "\nCombo Mechanic:\nOnce per game,\nIf two combinable Bakugan land on the same Gate Card, and one is less than 500 G power, \nYou may combine these two Bakugan, adding both of their G-Powers together.\nIt can be considered dual attribute if the two attributes of the Bakugan are different.\nThis combination lasts until the battle with this combination is finished.\nAfter Battle, these Bakugan unfuse and are placed in your used pile."
EVO_COMBO_MECHANIC = "\nEvo-Combo Mechanic:\nPlay before you roll and have a standing a Bakugan of the same attribute or type on a gate card. \nIf this evolution is in your unused pile, you may replace the Bakugan stood on the gate card with this Bakugan.\nPut the old Bakugan into this pile, and put the evolution in your used pile after battle.\nThis Bakugan goes through the regular used and unused pile cycle with other Bakugan, and counts as one of the three (or six in the big game) Bakugan you are allowed. \n\nIf another combinable Bakuagn lands on this gate card, use the Combo Mechanic rule, ignoring the 'once per game limiter.'\n\nCombo Mechanic:\nOnce per game,\nIf two combinable Bakugan land on the same Gate Card, and one is less than 500 G power, \nYou may combine these two Bakugan, adding both of their G-Powers together.\nIt can be considered dual attribute if the two attributes of the Bakugan are different.\nThis combination lasts until the battle with this combination is finished.\nAfter Battle, these Bakugan unfuse and are placed in your used pile."
VEXOS_EVO_RULES = "\nVEXOS Evolutions:\nPlay before you roll a Bakugan with a HEX Card,\nYou may Super Evolve this Bakugan. \nDuring Battle, you may play the ability located on the back of the Bakugan's character card.\n\nIf the Bakugan is an EVO-COMBO Bakugan, you may play using the EVO COMBO Rules instead,\nAnd your Bakugan may still play the ability on the back of its character card.\n\nEvo-Combo Mechanic:\nPlay before you roll and have a standing a Bakugan of the same attribute or type on a gate card. \nIf this evolution is in your unused pile, you may replace the Bakugan stood on the gate card with this Bakugan.\nPut the old Bakugan into this pile, and put the evolution in your used pile after battle.\nThis Bakugan goes through the regular used and unused pile cycle with other Bakugan, and counts as one of the three (or six in the big game) Bakugan you are allowed. \n\nIf another combinable Bakuagn lands on this gate card, use the Combo Mechanic rule, ignoring the 'once per game limiter.'\n\nCombo Mechanic:\nOnce per game,\nIf two combinable Bakugan land on the same Gate Card, and one is less than 500 G power, \nYou may combine these two Bakugan, adding both of their G-Powers together.\nIt can be considered dual attribute if the two attributes of the Bakugan are different.\nThis combination lasts until the battle with this combination is finished.\nAfter Battle, these Bakugan unfuse and are placed in your used pile."

ATTRIBUTE_LIST = ["pyrus", "pyrus2", "pyrus3", "subterra", "subterra2", "aurelus", "haos", "haos2", "haos3", "aquos", "aquos2", "aquos3", "darkus", "darkus2", "darkus3", "ventus", "ventus2", "ventus3", "genesis", "diamond", "diamond2", "clear", "nulltype", "galaxy"]
ATTRIBUTE_RESPONSE = [PYRUS1, PYRUS2, PYRUS3, SUBTERRA1, SUBTERRA2, AURELUS, HAOS1, HAOS2, HAOS3, AQUOS1, AQUOS2, AQUOS3, DARKUS1, DARKUS2, DARKUS3, VENTUS1, VENTUS2, VENTUS3, ALLFACTION, DIAMOND1, DIAMOND2, CLEAR_ATTRIBUTE, NOATTRIBUTE, GALAXY]

SPECIAL_COLOR_LIST = ["clear", "translucent", "dual_attribute", "pearl", "flip", "bakucore", "solar", "blue", "camo", "exoskin", "metalix", "stand", "crimson_pearl", "eviltwin"]
SPECIAL_COLOR_RESPONSE = [CLEAR_RULE, TRANSLUCENT, DUAL_ATTRIBUTE, PEARL, FLIP, BAKUCORE, SOLAR, BAKUBLUE, BAKUCAMO, EXOSKIN, BAKUMETALIX, BAKUSTAND, CRIMSONPEARL, EVILTWIN]

SPECIAL_ATTACK_LIST = ["heavy_metal", "spin", "attribute_dice", "gpower_dice", "jumping", "ripcord", "lightup", "bakutremor", "bakuvice", "double_magnet", "double_strike", "sky_gaia", "sky_raiders"]
SPECIAL_ATTACK_RESPONSE = [HEAVY_METAL, SPIN, ATTRIBUTE_DICE, GPOWER_DICE, JUMPING, RIPCORD, LIGHTUP, BAKUTREMOR, BAKUVICE, DOUBLE_MAGNET, DOUBLE_STRIKE, SKY_GAIA_ATTACK, SKY_RAIDERS_ATTACK]

SPECIAL_RULES_LIST = ["sky_gaia", "sky_raiders", "evolution", "super_evolution", "battle_compatible", "bakugear_compatible", "nano_compatible", "bakumutant", "bakubind", "synchro", "bakufusion", "combo", "evo_combo", "vexos_evo"]
SPECIAL_RULES_RESPONSE = [SKY_GAIA_RULES, SKY_RAIDERS_RULES, EVOLUTION_RULE, SUPER_EVOLUTION_RULES, BATTLE_GEAR_COMPATIBLE, BAKU_GEAR_COMPATIBLE, NANO_COMPATIBLE, BAKUMUTANT_RULES, BAKUBIND_RULES, SYNCHRO_BAKUGAN_RULES, BAKUFUSION_RULES, COMBO_MECHANIC, EVO_COMBO_MECHANIC, VEXOS_EVO_RULES]

# Class for Bakugan: Parameters: (name, g-power, attribute, type, special_color=None, special_attack=None, special_rules=None)
class Bakugan:
    __slots__ = ["__name", "__g_power", "__attribute", "__type", "__special_color", "__special_attack", "__special_rules"]
    def __init__(self, name, g, attribute, type, special_color=None, special_attack=None, special_rules=None, second_attribute=None):
        self.__name = name
        self.__g_power = g
        self.__attribute = [attribute]
        self.__type = type
        self.__special_color = special_color
        self.__special_attack = special_attack
        self.__special_rules = special_rules
        if second_attribute != None:
            self.__attribute.append(second_attribute)
    
    def get_name(self):
        return self.__name
    def get_g_power(self):
        return str(self.__g_power)
    def get_attribute(self):
        return_string = ""
        for item in range(len(self.__attribute)):
            return_string += self.__attribute[item]
        return return_string
    def get_type(self):
        return self.__type
    def get_special_color(self):
        return self.__special_color
    def get_special_attack(self):
        return self.__special_attack
    def get_special_rules(self):
        return self.__special_rules
    
    def get_attribute_info(self):
        """
        For each attribute in the attribute list, will return the designated string for each attribute
        Attributes are pyrus1, pyrus2, pyrus3, subterra1, subterra2, aurelus, haos1, haos2, haos3, aquos1, aquos2, aquos3, darkus1, darkus2, darkus3, ventus1, ventus2, ventus3, diamon1, diamond2, clear, nulltype, galaxy.
        """
        
        attribute_string = ""
        for index in range(len(ATTRIBUTE_LIST)):
            if ATTRIBUTE_LIST[index] == self.get_attribute():
                attribute_string += ATTRIBUTE_RESPONSE[index]
        return attribute_string
    
    def get_special_info(self):
        """
        Will return any special information relating to this Bakugan, if any
        """
        special_string = ""
        if self.get_special_color() != None or self.get_special_color() != "None":
            # Adds to the string depending on special color info
            for index in range(len(SPECIAL_COLOR_LIST)):
                if SPECIAL_COLOR_LIST[index] == self.get_special_color():
                    special_string += SPECIAL_COLOR_RESPONSE[index]
                    special_string += "\n\n"
        
        if self.get_special_attack() != None or self.get_special_attack() != "None":
            # Adds to the string depending on special attack info
            for index in range(len(SPECIAL_ATTACK_LIST)):
                if SPECIAL_ATTACK_LIST[index] == self.get_special_attack():
                    special_string += SPECIAL_ATTACK_RESPONSE[index]
                    special_string += "\n"
        
        if self.get_special_rules() != None or self.get_special_rules() != "None":
            # Adds to the string depending on special ruleset
            for index in range(len(SPECIAL_RULES_LIST)):
                if SPECIAL_RULES_LIST[index] == self.get_special_rules():
                    special_string += SPECIAL_RULES_RESPONSE[index]

        return special_string
    def display_basic(self):
        return self.get_name() + " " + self.get_attribute() + " " + self.get_g_power()
    # __str__ function to give a full output for the Bakugan
    def __str__(self):
        return_string = self.get_name() + ", " + self.get_g_power() + ", " + self.get_type() + "\n" + "Attribute: " + self.get_attribute_info() + "\n\n" + self.get_special_info()
        return return_string

def make_bakugan():
    name = input("What is the Bakugan's name? ")
    g_power = input("What is the Bakugan's G Power? ")
    b_attribute = input("What is the Bakugan's Attribute? ")
    b_type = None
    color_prompt = input("Any special color scheme? (Y/N): ")
    if color_prompt.lower() == "y":
        b_special_color = input("What is the color scheme? ")
    else:
        b_special_color = None
    attack_prompt = input("Any special attack? (Y/N): ")
    if attack_prompt.lower() == "y":
        b_special_attack = input("What is the attack mechanic? ")
    else:
        b_special_attack = None
    rules_prompt = input("Any special ruleset? (Y/N): ")
    if rules_prompt.lower() == "y":
        b_special_rules = input("What is the ruleset? ")
    else:
        b_special_rules = None
    new_bakugan = Bakugan(name, g_power, b_attribute, b_type, special_color=b_special_color, special_attack=b_special_attack, special_rules=b_special_rules)
    return new_bakugan

# Makes a list of Bakugan known
def create_bakugan_database(bakugan_csv):
    """
    Using a csv file, returns a list of Bakugan with a number identifier, and it creates the list with each Bakugan
    """
    # Class for Bakugan: Parameters: (name, g-power, attribute, type, special_color=None, special_attack=None, special_rules=None)
    bakugan_dict = dict()
    with open(bakugan_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        i = 0
        for row in csv_reader:
            bakugan_dict[str(i+1)] = Bakugan(row[0], row[1], row[2], row[3], special_color=row[4], special_attack=row[5], special_rules=row[6])
            i += 1
    return bakugan_dict

# Main function
def main():
    """
    The main function
    """
    # user_bakugan = make_bakugan()
    # print(user_bakugan)
    new_bakugan = Bakugan("Dragaon", "200", "galaxy", "dragon", special_color="eviltwin", special_attack="sky_raiders", special_rules="vexos_evo")
    print(new_bakugan)
    bakugan_dict = create_bakugan_database("CardIdentifier/Bakugan/text/bakugan_sample.csv")
    print(bakugan_dict["71"])
    print(bakugan_dict["1"])
    print(bakugan_dict["121"])

# Run guard
if __name__ == "__main__":
    main()