"""
Version 0.0.0.0.1.0
Things to do:
Saving/Loading
Evasion, Accuracy, and Critical Rate
"""
import random
#Classes
class Character:
    def __init__(self, Str, dex, vit, ene, Gold, Name):
        self.strength = Str
        self.dexterity = dex
        self.vitality = vit
        self.energy = ene
        self.maxHealth = vit * 20
        self.health = self.maxHealth
        self.maxMana = ene * 10
        self.mana = self.maxMana
        self.defense = Str * 1.5
        self.magdef = ene * 1.5
        self.atkMeleeMin = Str * 4
        self.atkMeleeMax = Str * 6
        self.atkRangedMin = dex * 4
        self.atkRangedMax = dex * 6
        self.atkMagicMin = ene * 4
        self.atkMagicMax = ene * 6
        self.gold = Gold
        self.name = Name
        #not implemented
        self.evasion = dex * 5
        self.accuracy = dex * 5
        self.criticalRate = ((dex + (Str/2))/2) * 5
        #not implemented
        
    def getAttackPhrase(self, Type):
        if self.name is "Goblin":
            if Type == "physical":
                return "The "+str(self.name)+" looks around stupidly and decides to attack you."
            if Type == "magic":
                return "The "+str(self.name)+" looks around cleverly and decides to cast a spell."
        if self.name is "Dog":
            if Type == "physical":
                return "The "+str(self.name)+" charges and bites you in the arm."
            if Type == "magic":
                return "The "+str(self.name)+" jumps around looking cute, and casts a spell."
        if self.name is "Bunny":
            if Type == "physical":
                return "The "+str(self.name)+" jumps around looking cute, and jumps at you."
            if Type == "magic":
                return "The "+str(self.name)+" jumps around looking cute, and casts a spell."

    def getRawMeleeDamage(self):
        return random.randint(self.atkMeleeMin,self.atkMeleeMax)
    def getRawRangedDamage(self):
        return random.randint(self.atkRangedMin,self.atkRangedMax)
    def getRawMagicDamage(self):
        return random.randint(self.atkMagicMin,self.atkMagicMax)

    def receivePhyDamage(self, dmg):
        if dmg > self.defense:
            self.health -= dmg + self.defense
        if self.health < 0:
            self.health = 0
    def receiveMagDamage(self, dmg):
        if dmg > self.magdef:
            self.health -= dmg + self.magdef
        if self.health < 0:
            self.health = 0
#Update
    def stats(self):
        self.maxHealth = self.vitality * 20
        self.maxMana = self.energy * 10
        self.defense = self.strength * 1.5
        self.magdef = self.energy * 1.5
        self.atkMeleeMin = self.strength * 4
        self.atkMeleeMax = self.strength * 6
        self.atkRangedMin = self.dexterity * 4
        self.atkRangedMax = self.dexterity * 6
        self.atkMagicMin = self.energy * 4
        self.atkMagicMax = self.energy * 6
        #not implemented
        self.evasion = self.dexterity * 5
        self.accuracy = self.dexterity * 5
        self.criticalRate = ((self.dexterity + (self.strength/2))/2) * 5
        #not implemented
#Attributes
atrMain00=["Contine","New Game","Load Game","Options","Exit Game"]
atrGen00=["Yes","No"]
atrAdv=["Attack","Defend","Item","Run"]
atrAtt=["Melee","Ranged","Magic"]
atr00=["Adventure","Train","Sleep"]
atr01=["Str","Dex","Vit","Ene","Nevermind"]
#Monsters
MonstersAtr00=["Goblin","Dog","Bunny"]
mons=2
#Main Menu
def mainMenu():
    print """
    1) Continue
    2) New Game
    3) Load Game
    4) Options
    5) Tutorial
    6) Credits
    7) Exit Game
        """
    choice = 0
    while choice < 1 or choice > 7:
        try:
            choice = int(raw_input(" > "))
        except ValueError:
            continue
    if choice == 1:
        mainMenu()
    if choice == 2:
        print "Introduction:\nAnd so it begins, the journey of a thousand steps."
    if choice == 3:
        mainMenu()
    if choice == 4:
        print "There are no current options."
        mainMenu()
    if choice == 5:
        print "Tutorial:\n You have 4 stats: Strength, Dexterity, Vitality, and Energy. Strength increases Melee Damage and Defense. Dexterity increases Ranged Damage. Vitality increases Health. Energy increases Mana, Magic Damage, and Magic Defense."
        mainMenu()
    if choice == 6:
        print "Contributors:"
        print "David Le\nGia Lan Cao\nAlvin Nguyen\nVictor Le\nThuong Nguyen"
        mainMenu()
    if choice == 7:
        quit(1)
#Main Menu
print "##########################"
print "#Dungeons Without Dragons#"
print "##########################"
mainMenu()
#Program Starts
Name=raw_input("What will you be known as? ")
player = Character(5,5,5,5,100,Name)
print"Welcome to Dungeons Without Dragons, %s!" %player.name
print"Welcome to town! Here, you can go adventuring,train your skills, or sleep and restore your health and mana."
while True:
    print
    print"Stats:"
    print("Strength:"+str(player.strength))
    print("Dexterity:"+str(player.dexterity))
    print("Vitality:"+str(player.vitality))
    print("Energy:"+str(player.energy))
    print("Health:"+str(player.health)+"/"+str(player.maxHealth))
    print("Mana:"+str(player.mana)+"/"+str(player.maxMana))
    print("Defense:"+str(player.defense))
    print("Magic Defense:"+str(player.magdef))
    print "Evasion:"+str(player.evasion)
    print "Accuracy:"+str(player.accuracy)
    print "Critical Rate:"+str(player.criticalRate)
    print("Gold:"+str(player.gold))
    Town=raw_input("What would you like to do?(Adventure,Train,Sleep) ")
    while Town not in atr00:
        print"You decide to waste time, wandering the city."
        Town=raw_input("What would you like to do?(Adventure,Train,Sleep) ")
    #Fighting
    if Town==atr00[0]:
        inBattle = True
        while inBattle:
            n=random.randint(0,mons)
            print "You have encountered a "+MonstersAtr00[n]+"."
            if n==0:
                monster = Character(2,1,3,1,30,"Goblin")
                while monster.health>0 and player>0:
                    battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run) ")
                    while battleActions not in atrAdv:
                        print"What? You can't do that!"
                        battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run) ")
                    if battleActions==atrAdv[0]:
                        attackType=raw_input("What type of attack do you want to do?(Melee,Ranged,Magic) ")
                        while attackType not in atrAtt:
                            print"Never heard of that move, let's stick to what we know."
                            attackType=raw_input("What type of attack do you want to do?(Melee,Ranged,Magic) ")
                        if attackType==atrAtt[0]:
                            print"You take a swing with your sword."
                            monster.receivePhyDamage(player.getRawMeleeDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("physical")
                            player.receivePhyDamage(monster.getRawMeleeDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if attackType==atrAtt[1]:
                            print"You fire an arrow."
                            monster.receivePhyDamage(player.getRawRangedDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("physical")
                            player.receivePhyDamage(monster.getRawMeleeDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if attackType==atrAtt[2]:
                            print"You decide to cast a spell."
                            monster.receiveMagDamage(player.getRawMagicDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("physical")
                            player.receivePhyDamage(monster.getRawMeleeDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                    if battleActions==atrAdv[1]:
                        defenseType=raw_input("What type of defense do you want to do?(Melee,Ranged,Magic) ")
                        while defenseType not in atrAtt:
                            print"Never heard of that move, let's stick to what we know."
                            defenseType=raw_input("What type of defense do you want to do?(Melee,Ranged,Magic) ")
                        if defenseType==atrAtt[0]:
                            print"You decide to raise your shield."
                            player.defense *= 1.5
                            print monster.getAttackPhrase("physical")
                            player.defense /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if defenseType==atrAtt[1]:
                            print"You jump on your toes, ready to dodge an arrow."
                            player.defense *= 1.5
                            print monster.getAttackPhrase("physical")
                            player.defense /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if defenseType==atrAtt[2]:
                            print"You cast a ward, shielding yourself from magical attacks."
                            player.magdef *= 1.5
                            print monster.getAttackPhrase("physical")
                            player.magdef /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                    if battleActions==atrAdv[2]:
                        print"You have no items. You should wait until future patches."
                        battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run) ")
                    if battleActions==atrAdv[3]:
                        print"You grab your gear and run off towards town."
                        inBattle = False
                if player.health<=0:
                    print"You have died."
                    print"You wake up in town."
                    inBattle = False
                elif monster.health<=0:
                    print("You have slain the "+monster.name+".")
                    print"You decide to head back to town."
                    player.gold+=monster.gold
                    print("You have found " + str(monster.gold) + " gold!")
                    inBattle = False
            if n==1:
                monster = Character(3,1,2,1,20,"Dog")
                while monster.health>0 and player>0:
                    battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run) ")
                    while battleActions not in atrAdv:
                        print"What? You can't do that!"
                        battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run) ")
                    if battleActions==atrAdv[0]:
                        attackType=raw_input("What type of attack do you want to do?(Melee,Ranged,Magic) ")
                        while attackType not in atrAtt:
                            print"Never heard of that move, let's stick to what we know."
                            attackType=raw_input("What type of attack do you want to do?(Melee,Ranged,Magic) ")
                        if attackType==atrAtt[0]:
                            print"You take a swing with your sword."
                            monster.receivePhyDamage(player.getRawMeleeDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("physical")
                            player.receivePhyDamage(monster.getRawMeleeDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if attackType==atrAtt[1]:
                            print"You fire an arrow."
                            monster.receivePhyDamage(player.getRawRangedDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("physical")
                            player.receivePhyDamage(monster.getRawMeleeDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if attackType==atrAtt[2]:
                            print"You decide to cast a spell."
                            monster.receiveMagDamage(player.getRawMagicDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("physical")
                            player.receivePhyDamage(monster.getRawMeleeDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                    if battleActions==atrAdv[1]:
                        defenseType=raw_input("What type of defense do you want to do?(Melee,Ranged,Magic) ")
                        while defenseType not in atrAtt:
                            print"Never heard of that move, let's stick to what we know."
                            defenseType=raw_input("What type of defense do you want to do?(Melee,Ranged,Magic) ")
                        if defenseType==atrAtt[0]:
                            print"You decide to raise your shield."
                            player.defense *= 1.5
                            print monster.getAttackPhrase("physical")
                            player.defense /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if defenseType==atrAtt[1]:
                            print"You jump on your toes, ready to dodge an arrow."
                            player.defense *= 1.5
                            print monster.getAttackPhrase("physical")
                            player.defense /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if defenseType==atrAtt[2]:
                            print"You cast a ward, shielding yourself from magical attacks."
                            player.magdef *= 1.5
                            print monster.getAttackPhrase("physical")
                            player.magdef /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                    if battleActions==atrAdv[2]:
                        print"You have no items. You should wait until future patches."
                        battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run)")
                    if battleActions==atrAdv[3]:
                        print"You grab your gear and run off towards town."
                        inBattle = False
                if player.health<=0:
                    print"You have died."
                    print"You wake up in town."
                    inBattle = False
                elif monster.health<=0:
                    print("You have slain the "+monster.name+".")
                    print"You decide to head back to town."
                    player.gold+=monster.gold
                    print("You have found " + str(monster.gold) + " gold!")
                    inBattle = False
            if n==2:
                monster = Character(1,1,1,3,10,"Bunny")
                while monster.health>0 and player>0:
                    battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run)")
                    while battleActions not in atrAdv:
                        print"What? You can't do that!"
                        battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run)")
                    if battleActions==atrAdv[0]:
                        attackType=raw_input("What type of attack do you want to do?(Melee,Ranged,Magic)")
                        while attackType not in atrAtt:
                            print"Never heard of that move, let's stick to what we know."
                            attackType=raw_input("What type of attack do you want to do?(Melee,Ranged,Magic)")
                        if attackType==atrAtt[0]:
                            print"You take a swing with your sword."
                            monster.receivePhyDamage(player.getRawMeleeDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("magic")
                            player.receiveMagDamage(monster.getRawMagicDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if attackType==atrAtt[1]:
                            print"You fire an arrow."
                            monster.receivePhyDamage(player.getRawRangedDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("magic")
                            player.receiveMagDamage(monster.getRawMagicDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if attackType==atrAtt[2]:
                            print"You decide to cast a spell."
                            monster.receiveMagDamage(player.getRawMagicDamage())
                            print monster.name+":"+ str(monster.health) + "/" + str(monster.maxHealth)
                            print monster.getAttackPhrase("magic")
                            player.receiveMagDamage(monster.getRawMagicDamage())
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                    if battleActions==atrAdv[1]:
                        defenseType=raw_input("What type of defense do you want to do?(Melee,Ranged,Magic) ")
                        while defenseType not in atrAtt:
                            print"Never heard of that move, let's stick to what we know."
                            defenseType=raw_input("What type of defense do you want to do?(Melee,Ranged,Magic) ")
                        if defenseType==atrAtt[0]:
                            print"You decide to raise your shield."
                            player.defense *= 1.5
                            print monster.getAttackPhrase("magic")
                            player.defense /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if defenseType==atrAtt[1]:
                            print"You jump on your toes, ready to dodge an arrow."
                            player.defense *= 1.5
                            print monster.getAttackPhrase("magic")
                            player.defense /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                        if defenseType==atrAtt[2]:
                            print"You cast a ward, shielding yourself from magical attacks."
                            player.magdef *= 1.5
                            print monster.getAttackPhrase("magic")
                            player.magdef /= 1.5
                            print player.name+":"+ str(player.health) + "/" + str(player.maxHealth)
                    if battleActions==atrAdv[2]:
                        print"You have no items. You should wait until future patches."
                        battleActions=raw_input("What would you like to do?(Attack,Defend,Item,Run) ")
                    if battleActions==atrAdv[3]:
                        print"You grab your gear and run off towards town."
                        inBattle = False
                if player.health<=0:
                    print"You have died."
                    print"You wake up in town."
                    inBattle = False
                elif monster.health<=0:
                    print("You have slain the "+monster.name+".")
                    print"You decide to head back to town."
                    player.gold+=monster.gold
                    print("You have found " + str(monster.gold) + " gold!")
                    inBattle = False
    #Training
    if Town==atr00[1]:
        inTraining = True
        while inTraining:
            Training=raw_input("What would you like to train?(Str,Dex,Vit,Ene)It costs 15 Gold. Or do you wish to leave?(Nevermind) ")
            while Training not in atr01:
                Training=raw_input("What would you like to train?(Str,Dex,Vit,Ene)It costs 15 Gold. Or do you wish to leave?(Nevermind) ")
            if Training==atr01[0]:
                player.strength+=1
                print("Strength:"+str(player.strength))
                player.defense=player.strength*1.5
                print("Defense:"+str(player.defense))
                player.atkMeleeMin=player.strength*4
                player.atkMeleeMax=player.strength*6
                print("Attack(Melee):"+str(player.atkMeleeMin)+"-"+str(player.atkMeleeMax))
                player.gold-=15
                print("Gold:"+str(player.gold))
                Retrain=raw_input("Would you like to keep training?(Yes,No)")
                while Retrain not in atrGen00:
                   Retrain=raw_input("Would you like to keep training?(Yes,No)")
                if Retrain==atrGen00[0]:
                    print"Ok!"
                if Retrain==atrGen00[1]:
                    inTraining = False
            if Training==atr01[1]:
                player.dexterity+=1
                print("Dexterity:"+str(player.dexterity))
                player.evasion = player.dexterity * 5
                print "Evasion:"+str(player.evasion)
                player.accuracy = player.dexterity * 5
                print "Accuracy:"+str(player.accuracy)
                player.criticalRate = ((player.dexterity + (player.strength/2))/2) * 5
                print "Critical Rate:"+str(player.criticalRate)
                player.atkRangedMin=player.dexterity*4
                player.atkRangedMax=player.dexterity*6
                print("Attack(Ranged):"+str(player.atkRangedMin)+"-"+str(player.atkRangedMax))
                player.gold-=15
                print("Gold:"+str(player.gold))
                Retrain=raw_input("Would you like to keep training?(Yes,No) ")
                while Retrain not in atrGen00:
                   Retrain=raw_input("Would you like to keep training?(Yes,No) ")
                if Retrain==atrGen00[0]:
                    print"Ok!"
                if Retrain==atrGen00[1]:
                    inTraining = False
            if Training==atr01[2]:
                player.vitality+=1
                print("Vitality:"+str(player.vitality))
                player.maxHealth=player.vitality*20
                player.health=player.maxHealth
                print("Health:"+str(player.health)+"/"+str(player.maxHealth))
                player.gold-=15
                print("Gold:"+str(player.gold))
                Retrain=raw_input("Would you like to keep training?(Yes,No) ")
                while Retrain not in atrGen00:
                   Retrain=raw_input("Would you like to keep training?(Yes,No) ")
                if Retrain==atrGen00[0]:
                    print"Ok!"
                if Retrain==atrGen00[1]:
                    inTraining = False
            if Training==atr01[3]:
                player.energy+=1
                print("Energy:"+str(player.energy))
                player.maxMana=player.energy*10
                player.mana=player.maxMana
                print("Mana:"+str(player.mana)+"/"+str(player.maxMana))
                player.magDef=player.energy*1.5
                print("Magic Defense:"+str(player.magdef))
                player.atkMagicMin=player.energy*4
                player.atkMagicMax=player.energy*6
                print("Attack(Magic):"+str(player.atkMagicMin)+"-"+str(player.atkMagicMax))
                player.gold-=15
                print("Gold:"+str(player.gold))
                Retrain=raw_input("Would you like to keep training?(Yes,No) ")
                while Retrain not in atrGen00:
                   Retrain=raw_input("Would you like to keep training?(Yes,No) ")
                if Retrain==atrGen00[0]:
                    print"Ok!"
                if Retrain==atrGen00[1]:
                    inTraining = False
            if Training==atr01[4]:
                print "Alright then, see you around."
                inTraining = False
    #Sleeping
    if Town==atr00[2]:
        inSleeping = True
        while inSleeping:
            print("Health:"+str(player.health)+"/"+str(player.maxHealth))
            print("Mana:"+str(player.mana)+"/"+str(player.maxMana))
            Sleeping=raw_input("Would you like to spend the night at an Inn? It will restore your health and mana to max. It costs 10 Gold.(Yes,No) ")
            while Sleeping not in atrGen00:
                Sleeping=raw_input("Would you like to spend the night at an Inn? It will restore your health and mana to max. It costs 10 Gold.(Yes,No) ")
            if Sleeping==atrGen00[0]:
                player.health=player.maxHealth
                player.mana=player.maxMana
                print("Health:"+str(player.health)+"/"+str(player.maxHealth))
                print("Mana:"+str(player.mana)+"/"+str(player.maxMana))
                player.gold-=10
                print("Gold:"+str(player.gold))
                inSleeping = False
            if Sleeping==atrGen00[1]:
                print "Alright then, see you around."
                inSleeping = False
#Program End
