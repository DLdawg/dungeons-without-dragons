file = open('SUVGAMLULS.4chanpartyvan', 'r')

strengthOnFile = 0

dexterityOnFile = 10

vitalityOnFile = 20

energyOnFile = 30

maxHealthOnFile = 40

healthOnFile = 50

maxManaOnFile = 60

manaOnFile = 70

defenseOnFile = 80

magdefOnFile = 90

atkMeleeMinOnFile = 100

atkMeleeMaxOnFile = 110

atkRangedMinOnFile = 120

atkRangedMaxOnFile = 130

atkMagicMinOnFile = 140

atkMagicMaxOnFile = 150

goldOnFile = 160

evasionOnFile = 170

accuracyOnFile = 180

criticalRateOnFile = 190

nameOnFile = 20000

file.seek(strengthOnFile)
player.strength = int(file.read(10))

file.seek(dexterityOnFile)
player.dexterity = int(file.read(10))

file.seek(vitalityOnFile)
player.vitality = int(file.read(10))

file.seek(energyOnFile)
player.energy = int(file.read(10))

file.seek(maxHealthOnFile)
player.maxHealth = int(file.read(10))

file.seek(healthOnFile)
player.health = int(file.read(10))

file.seek(maxManaOnFile)
player.maxMana = int(file.read(10))

file.seek(manaOnFile)
player.mana = int(file.read(10))

file.seek(defenseOnFile)
player.defense = int(file.read(10))

file.seek(magdefOnFile)
player.magdef = int(file.read(10))

file.seek(atkMeleeMinOnFile)
player.atkMeleeMin = int(file.read(10))

file.seek(atkMeleeMaxOnFile)
player.atkMeleeMax = int(file.read(10))

file.seek(atkRangedMinOnFile)
player.atkRangedMin = int(file.read(10))

file.seek(atkRangedMaxOnFile)
player.atkRangedMax = int(file.read(10))

file.seek(atkMagicMinOnFile)
player.atkMagicMin = int(file.read(10))

file.seek(atkMagicMaxOnFile)
player.atkMagicMax = int(file.read(10))

file.seek(goldOnFile)
player.gold = int(file.read(10))

file.seek(evasionOnFile)
player.evasion = int(file.read(10))

file.seek(accuracyOnFile)
player.accuracy = int(file.read(10))

file.seek(criticalRateOnFile)
player.criticalRate = int(file.read(10))

file.seek(nameOnFile)
player.name = file.read()
