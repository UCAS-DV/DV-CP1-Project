import random
global playerHP
global playerAtk
global playerDef
global inventory
global equipped
global roomNineCleared
global roomTwelveCleared
global bootGot
global potionGot
playerHP = 100
playerDef = 5
playerAtk = 5
inventory = ['Steel Shortsword', 'Tin Helmet']
equipped = ['Steel Shortsword', 'Tin Helmet']
roomNineCleared = False
roomTwelveCleared = False
bootGot = False
potionGot = False

def inventoryChoices():
    global playerAtk
    global playerDef
    global inventory
    global equipped
    while True:
        print("\nYou have:")
        for item in inventory:
            print(item)
        print('\nYour equipped items are:')
        for item in equipped:
            print(item)
        playerChoice = input("\nWelcome to your inventory!\n1:Equip new items(You can have multiple armor pieces, but only one weapon at a time.)\n2:Unequip items\n3:Exit\nChoose:")
        if playerChoice == '1':
            while True:
                itemChoice = input("\nWhat item would you like to equip?\nChoose:").title()
                if itemChoice in equipped:
                    print("\nSorry, you already have that equipped. Try again!")
                    break
                if itemChoice not in inventory:
                    print("\nSorry, that's not a valid item.")
                    break
                elif itemChoice == 'Steel Shortsword':
                    playerAtk = 10
                    try: 
                        equipped.pop(equipped.index('Tick Slaying Blade'))
                    except:
                        pass
                    try:
                        equipped.pop(equipped.index('Blade Of Angst'))
                    except:
                        pass
                    equipped.append("Steel Shortsword")
                    break
                elif itemChoice == 'Tick Slaying Blade':
                    playerAtk = 15
                    try: 
                        equipped.pop(equipped.index('Steel Shortsword'))
                    except:
                        pass
                    try:
                        equipped.pop(equipped.index('Blade Of Angst'))
                    except:
                        pass
                    equipped.append("Tick Slaying Blade")
                    break
                elif itemChoice == 'Blade Of Angst':
                    playerAtk = 20
                    try: 
                        equipped.pop(equipped.index('Tick Slaying Blade'))
                    except:
                        pass
                    try:
                        equipped.pop(equipped.index('Steel Shortsword'))
                    except:
                        pass
                    equipped.append("Blade Of Angst")
                    break
                elif itemChoice == 'Tin Helmet' or itemChoice == 'Radical Boots' or itemChoice == 'Lemon Rind Chestplate':
                    playerDef += 5
                    equipped.append(itemChoice)
                    break
                else:
                    print("\nSorry, that's not a valid item. Try again.")
                    break
        elif playerChoice == '2':
            while True:
                itemChoice = input("What would you like to unequip?").title()
                if itemChoice not in inventory:
                    print("\nYou don't have that item. Try again.")
                    break
                elif itemChoice not in equipped:
                    print("\nThat item isn't equipped!")
                    break
                elif itemChoice == 'Steel Shortsword':
                    playerAtk -= 9
                    equipped.pop(equipped.index(itemChoice))
                    break
                elif itemChoice == 'Tick Slaying Blade':
                    playerAtk -= 14
                    equipped.pop(equipped.index(itemChoice))
                    break
                elif itemChoice == 'Blade Of Angst':
                    playerAtk -= 19
                    equipped.pop(equipped.index(itemChoice))
                    break
                elif itemChoice == 'Tin Helmet' or itemChoice == 'Radical Boots' or itemChoice == 'Lemon Rind Chestplate':
                    playerDef -= 5
                    equipped.pop(equipped.index(itemChoice))
                    break
        elif playerChoice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nWrong number, nincompoop.")
def combat(enemyHP, enemyAtk):
    enemyCharge = False
    global playerAtk
    global playerDef
    global inventory
    global playerHP
    while True:
        if enemyCharge == True:
            print("\nYour enemy seems to be charging up.")
        print("\nYour opponent has:", enemyHP, "health points left.")
        print("\nYou have:", playerHP, "health points left.")
        playerChoice = input('\nWhat would you like to do?\n1:Attack\n2:Defend\n3:Item\nChoose:')
        if playerChoice == '1':
            enemyHP -= round((playerAtk)*round(random.uniform(0.7, 1), 2))
        elif playerChoice == '2':
            if enemyCharge == True:
                enemyCharge = False
            continue
        elif playerChoice == '3':
                while True:
                    print("\nYou have:")
                    for item in inventory:
                        print(item)
                    itemChoice = input("\nWhat item do you want to use?\nType exit to leave.\nChoose:").title()
                    if itemChoice == 'Healing Potion':
                        inventory.pop(inventory.index(itemChoice))
                        playerHP = 100
                        break
                    elif itemChoice == 'Amulet Of Rage':
                        inventory.pop(inventory.index(itemChoice))
                        playerAtk += 3
                        break
                    elif itemChoice == 'Exit':
                        break
                    else:
                        print("\nThat item isn't valid.")
                        continue
        else:
            print("\nWrong number, try again.")
        enemyChoice = random.randint(1,2)
        if enemyChoice == 1:
            
            if enemyCharge == True:
                dmg = round(((enemyAtk*2)-playerDef)*round(random.uniform(0.5, 1), 2))
                if dmg <= 0:
                    dmg = 0
                playerHP -= dmg
            else:
                dmg = round((enemyAtk-playerDef)*round(random.uniform(0.5, 1), 2))
                if dmg <= 0:
                    dmg = 0
                playerHP -= dmg
        elif enemyChoice == 2:
            enemyCharge = True
        if playerHP <= 0:
            return "Failed"
        elif enemyHP <= 0:
            return "Won"
        else:
            continue
def death():
    print("\nYou failed your mission and died. D:")
    exit()
def roomOne():
    print("\nYou are a slime named Beeyor.\nYour Mother's dog walker's dog walker's dog has a brain tumour, and you have been asked to retrieve a vial of the cure hidden in Wilson's dungeon,\nnamed after the legendary Wilson who first conquered it.\nYou will brave many dangers in order to fight Barry the Businessman, who guards the cure to the tumours.")
    print("\nAs you step off the ladder, you find yourself in a dark room with dank, smelly walls and nothing else of interest.\n")
    while True:
        playerChoice = input("\nWhat would you like to do?\n1:Go straight\n2:Go to the right\n3:Access inventory\nChoose:")
        if playerChoice == '1':
            roomTwo()
        elif playerChoice == '2':
            roomThree()
        elif playerChoice == '3':
            inventoryChoices()
        else:
            print("\nSorry, try again.")
def roomTwo():
    global inventory
    print("\nBefore you even enter the room, a pungent and unplesant aroma asaults your nose.\nIt would seem you find yourself in an ill-used and even less often cleaned bathroom.")
    print("\nBefore you can decide what to do next, you spot a potion in the medicine cabinet!\nHealing Potion obtained!")
    inventory.append('Healing Potion')
    while True:
        playerChoice = input("\nWhat would you like to do?\n1:Go straight\n2:Go right\n3:Access inventory\nChoose:")
        if playerChoice == '1':        
            roomFour()
        elif playerChoice == '2':
            roomFive()
        elif playerChoice == '3':
            inventoryChoices()
        else:
            print("\nSorry, try again.")
def roomThree():
    global inventory
    print("\nAs you walk through the seemingly empty room, a large tick about the size of a stove jumps out at you!")
    outcome = combat(25, 10)
    if outcome == 'Failed':
        death()
    elif outcome == 'Won':
        print("\n!As you pull your sword out of the tick's corpse, you notice something.")
        print("\nYou grab a sword from off a hook on the wall.\nTick Slaying Blade obtained!")
        inventory.append('Tick Slaying Blade')
        while True:    
            playerChoice = input("What would you like to do?\n1:Go Left\n2:Go Straight\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                roomFive()
            elif playerChoice == '2':
                roomSix()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, try again.")
def roomFour():
    print("\nIn your haste, you step into the room, only to discover it's filled with a deadly spike pit.")
    death()
def roomFive():
    print("\nIn the center of the room, a man in a chair turns to look at you. Gadzooks!\n It would seem an evil dentist desires a brawl!")
    outcome = combat(40, 15)
    if outcome == 'Failed':
        death()
    elif outcome == 'Won':
        print("\nWith a final strike, the evil dentist disolves into toothpaste.")
        while True:
            playerChoice = input("What would you like to do?\n1:Go Left\n2:Go Straight\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                roomSix()
            elif playerChoice == '2':
                roomSeven()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, try again.")
def roomSix():
    global inventory
    print("This room is lit with a beautiful lamp in the shape of an oversized lemon. As you admire the lamp, you realize this is not a lamp at all,\nrather an enemy encounter!")
    outcome = combat(70, 10)
    if outcome == 'Failed':
        death()
    elif outcome == 'Won':
        print("\nAs the lamp falls to the floor, its outer rind forms into a rock hard chestplate.\nYou obtained Lemon Rind Chestplate!")
        inventory.append("Lemon Rind Chestplate")
        while True:
            playerChoice = input("What would you like to do?\n1:Go Left\n2:Go Straight\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                roomSeven()
            elif playerChoice == '2':
                roomEight()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, try again.")
def roomSeven():
    global playerHP 
    print("You arrive at a room containing food, water and a bed.\nYou rested and recovered your health.")
    playerHP = 100
    while True:
        playerChoice = input("What do you want to do?\n1:Go straight\n2:Go Right\n3:Access Inventory\nChoose:")
        if playerChoice == '1':
            roomNine()
        elif playerChoice == '2':
            roomEight()
        elif playerChoice == '3':
            inventoryChoices()
        else:
            print("\nSorry, try again.")
def roomEight():
    global inventory
    print("When you carefully sneak into the room, you notice a depressed looking giraffe sulking in the corner.\n Before you can decide what to do, it turns it's head to look at you.")
    outcome = combat(10, 40)
    if outcome == 'Failed':
        death()
    elif outcome == 'Won':
        print("You hit the giraffe square in the neck, defeating it! Dejected, it hobbles back to its corner.")
        print('Hanging from a hook on the wall is a wicked looking blade with a grumpy aura surrounding it. You pick it up.\nYou obtained Blade of Angst!')
        inventory.append('Blade Of Angst')
        while True:
            playerChoice = input("What would you like to do?\n1:Go Left\n2:Go right\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                roomNine()
            elif playerChoice == '2':
                roomTwelve()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, Try again.")
def roomNine():
    global inventory
    global roomNineCleared
    if roomNineCleared == True:
        while True:
            playerChoice = input("What would you like to do?\n1:Go straight\n2:Go right\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                roomTen()
            elif playerChoice == '2':
                roomThirteen()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, try again.")
    else:
        print("Wow! A lovely sofa sits in the center of the room. As you prepare to take a rest on the wonderful piece of furniture, it shakes.\nThen it shakes more. It would seem this is a haunted sofa!")
        outcome = combat(30, 30)
        if outcome == 'Failed':
            death()
        elif outcome == 'Won':
            roomNineCleared = True
            print("With a twinge of regret, you stare at the torn cushions of the once-beautiful sofa.")
            print("After slaying the vicious sofa, you spot a gleam in between the cushions.\nYou obtained Amulet of Rage!")
            inventory.append("Amulet Of Rage")
            while True:
                playerChoice = input("What would you like to do?\n1:Look around\n2:Go Right\n3:Access Inventory\nChoose:")
                if playerChoice == '1':
                    print("As you look around the room, you realize that one of the walls is fake! You push the wall over to reveal a secret room!")
                    roomTen()
                elif playerChoice == '2':
                    roomThirteen()
                elif playerChoice == '3':
                    inventoryChoices()
                else:
                    print("\nSorry, try again.")
def roomTen():
    global inventory
    global bootGot
    if bootGot  == False:
        print("As you enter the room, you spot some glowing boots.\nYou got Radical Boots!")
        inventory.append("Radical Boots")
        bootGot = True
    while True:
        playerChoice = input("What would you like to do?\n1:Go back\n2:Go Left\n3:Access Inventory\nChoose:")
        if playerChoice == '1':
            roomNine()
        elif playerChoice == '2':
            roomThirteen()
        elif playerChoice == '3':
            inventoryChoices()
        else:
            print("\nSorry, try again.")
def roomEleven():
    global inventory
    global potionGot
    if potionGot  == False:
        print("As you enter the room, you spot a potion.\nYou got Potion Of Healing!")
        inventory.append("Potion Of Healing")
        potionGot = True
    while True:
        playerChoice = input("What would you like to do?\n1:Go back\n2:Go Left\n3:Access Inventory\nChoose:")
        if playerChoice == '1':
            roomTwelve()
        elif playerChoice == '2':
            roomThirteen()
        elif playerChoice == '3':
            inventoryChoices()
        else:
            print("\nSorry, try again.")
def roomTwelve():
    global roomTwelveCleared
    if roomTwelveCleared == True:
        while True:
            playerChoice = input("What would you like to do?\n1:Look around\n2:Go Left\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                print("As you look around the room, you realize that one of the walls is fake! You push the wall over to reveal a secret room!")
                roomEleven()
            elif playerChoice == '2':
                roomThirteen()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, try again.")
    else:
        print("You enter the room, only to be attacked by what seems to be a goat wearing a graduation cap!")
        outcome = combat(30, 5)
        if outcome == 'Failed':
            death()
        elif outcome == "Won":
            print("with a swipe of your sword, you knock the hat off of the goat's head.\nDisappointed, it wanders away.")
            roomTwelveCleared = True
            playerChoice = input("What would you like to do?\n1:Look around\n2:Go Left\n3:Access Inventory\nChoose:")
            if playerChoice == '1':
                print("As you look around the room, you realize that one of the walls is fake! You push the wall over to reveal a secret room!")
                roomEleven()
            elif playerChoice == '2':
                roomThirteen()
            elif playerChoice == '3':
                inventoryChoices()
            else:
                print("\nSorry, try again.")
def roomThirteen():
    print("You're finally here. The lair of Barry the Businessman. Time to end this.")
    outcome = combat(80, 40)
    if outcome == 'Failed':
        death()
    elif outcome == 'Won':
        print("You did it! Congratulations! You have successfully cured the tumours and brought peace to your mother's dog walker's dog walker's dog!")
        exit()
roomOne()