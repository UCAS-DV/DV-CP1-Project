import random
game_intro = '''
-~-~-~-~-~-~Quest for the Country!-~-~-~-~-~-~
           Enter Anything to Start
                      '''
  
position = 0
locations = [
    "Just a White Void",
    "Spookyland",
    "Area 51",
    "The Mythical State of North Dakota",
    "The North Pole",
    "The Roman Empire",
    "Town City",
    "British Texas",    
    "American Australia",
]
places_to_go = [
    # Just a White Void [0]
    [1, 2, 3, 4, 8],
    # Spookyland [1]
    [0, 4, 5, 6, 8],
    # Area 51 [2]
    [0, 3, 8],
    # The Mythical State of North Dakota [3]
    [0, 2, 4],
    # The North Pole [4]
    [0, 3, 5],
    # The Roman Empire [5]
    [1, 4, 6],
    # Town City [6]
    [1, 5, 7],
    # British Texas [7]
    [6, 8],
    # American Australia [8]
    [0, 1, 2, 7]
]
places_been = []

name = 'You'
inventory = []
player_stats = {
    "health": 100,
    "nerves": 85,
    "strength": 1,
    "bravery": 1,
    "durability": 1,
    "max_health": 100,
    "max_nerves": 85,
    "attack_potency": 1,
}
player_attacks = [
    {
        "name": "Uncouth Declaration",
        "damage": 0,
        "discomfort": 10,
        "description": '''Forget physical damage! Emotional damage is where it's at!
        Reduce your enemies NERVES by saying something mean to them!''',
        "super_success": ["Oh...", "wow...", "I get how intense this situation is but you didn't have to go that far.", "To be frank I don't even know if you can legally say that."],
        "success": ["Oh! He's absolutely devastated!"],
        "failure": ["Okay, so, pro tip...", 'Calling your opponent "Stinky" is not very effective past the first grade'],
        "super_failure": ["What was that?!", "That is likely the single most tame, polite sentence ever constructed"],
        "is_item": False
    }
]

items = [
    {
        "name": "High Hopes and Determination",
        "health_effect": 10,
        "nerves_effect": 30,
        "health_overtime_effect": 5,
        "nerves_overtime_effect": 10,
        "duration": 4,
        "to_player": True,
        "super_success": ["While on the ropes, it all comes back to you in a flash.", 
                         "You remember who you truly are.",
                         "You are not someone to be defeated by mere fatal injuries",
                         "This journey has reminded you that, not only you have friends and a family to come back to, but everyone in this country you've been fighting for has people to come back to as well",
                         "You are suddenly filled with high hopes and determination."],
        "success": ["Horrah! You're delusional sense of hope and determination has kicked in!"],
        "failure": ["Well, I mean, I guess that's a little better.", "You're still a little doomed, but hey, at least you're doomed with a smile on your face!"],
        "super_failure": ["Uh oh...", "Seems like you're attempted recall into your hopes and determination has just made you feel a little stupid", 
                          "Well, if it makes you feel better. I believe in you!",
                          "Well, that's actually lie, but your end is my end so please don't die."]
    }
]

bosses = [
    {
        "name": "The Voice in your Head",
        "health": 100,
        "max_health": 100,
        "nerves": 50,
        "max_nerves": 85,
        "attack_potency": 1,
        "victory_item": items[0],
        "location": 0,
        "intro": ["Battle GO!"],
        "boss_victory_text": ["Oh!", "How did you...", "I don't even exist!", "Wait, if you're gone, and I'm in your head, what does that mean for me?", "...", "Uh oh."],
        "boss_defeat_text": ["Wow! Bravo! Now that you know how to battle, it seems like you're ready to save the country and retrieve the pages!", 
                             "And don't worry, since I don't exist, I'm completely fine!", 
                             "I'll never leave..."],
        "is_defeated": False
    }
]

def Dialogue(dialogue = []):

    for line in dialogue:
        input(f'{line} ({dialogue.index(line) + 1}/{len(dialogue)})')
            
def RollNerveEffect(nerves):
    rolled_number = random.randint(1,100)

    if rolled_number > nerves:
        if rolled_number > (nerves * 1.5):
            return 0
        else:
            return 0.75
    else:
        if rolled_number < (nerves * 0.2):
            return 1.5
        else:
            return 1
        
def Move(current_local, desired_local):

    if desired_local == current_local:
        print(f"Um, are you crazy? {desired_local} doesn't exist. \nYou did not move.")
        return current_local
    elif locations[desired_local] not in locations:
        print(f"Um, you're already at {desired_local}. Congrats? \nYou did not move.")
        return current_local

    # On the chance the player is in Town City or American Australia, the game will verify whether or not they have a boat to determine if they succesfully move.
    if current_local in [6, 8]:
        if desired_local == 7:
            if "Boat" in inventory:
                print(f"Yar Har Har! You sailed the 7 seas! \nYou successfully moved to {locations[desired_local]}")
                return desired_local
            else:
                print(f'Unless your name is "Michael Fred Phelps," you are not making across the sea without a boat. \nYou did not move.')
                return current_local     
    
    # The game will check if the player can actually move to their desired_local from where they are. If they are, they can move, if not, they stay.
    if desired_local in places_to_go[current_local]:
        print(f"You successfully moved to {locations[desired_local]}")
        return desired_local
    else:
        print(f"Sorry pal, you can't move to {locations[desired_local]} from {locations[current_local]} \nYou did not move.")
        return current_local

def TakeAction(action, nerves_value, from_player, boss):
    nerve_multipler = RollNerveEffect(nerves_value)

    health_effect = 0
    nerves_effect = 0
    attack_health_effect = 0
    attack_nerves_effect = 0

    match nerve_multipler:
        case 0:
            Dialogue(action['super_failure'])
        case 0.75:
            Dialogue(action['failure'])
        case 1:
            Dialogue(action['success'])
        case 1.5:
            Dialogue(action['super_success'])

    if from_player:
        if action['is_item']:

            health_effect = action['health_effect'] * nerve_multipler
            nerves_effect = action['nerves_effect'] * nerve_multipler

            if action['to_player']:
                player_stats['health'] += health_effect
                player_stats['nerves'] += nerves_effect

                print(f'You healed {health_effect} health!')
                print(f'You gained {nerves_effect} nerves!')
            else:
                boss['health'] += health_effect
                boss['nerves'] += nerves_effect

                print(f'You dealt {health_effect} damage!')
                print(f'{boss['name']} lost {nerves_effect} nerves!')       
        else:

            attack_health_effect = action['damage'] * nerve_multipler
            attack_nerves_effect = action['discomfort'] * nerve_multipler

            boss['health'] -= attack_health_effect
            boss['nerves'] -= attack_nerves_effect

            print(f'You dealt {attack_health_effect} damage!')
            print(f'{boss['name']} lost {attack_nerves_effect} nerves!') 
    else:

        attack_health_effect = action['damage'] * nerve_multipler
        attack_nerves_effect = action['discomfort'] * nerve_multipler

        player_stats['health'] -= attack_health_effect
        player_stats['nerves'] -= attack_nerves_effect

        print(f'{boss['name']} dealt {attack_health_effect} damage to you.')
        print(f'You lost {attack_nerves_effect} nerves.')

def Fight(boss):
    turn = -1
    fight_finished = False

    while not fight_finished:
        if turn < 0:
            Dialogue(boss["intro"])
            turn += 1

        if turn % 2 == 0:
            print(f'-~-~-~-~-~{boss["name"]}-~-~-~-~-~ \n1. Check Stats \n2. Select Item \n3. Select Attack')
            try:
                action = int(input("What would you like to do (Enter Number)? "))
            except:
                input("Sorry, you entered that incorrectly. ")
                continue

            match action:
                case 1:
                    print("-=-=-=-Player Stats-=-=-=-")
                    print(f"Health: {player_stats["health"]}/{player_stats["max_health"]} \nNerves: {player_stats["nerves"]}/{player_stats["max_nerves"]} \nAttack Potency: {player_stats["attack_potency"]}x")
                    print(f"Durability {player_stats['durability']} \nBravery: {player_stats["bravery"]} \nStrength: {player_stats["strength"]}")
                    print("-=-=-=-Opponent Stats-=-=-=-")
                    print(f"Health: {boss['health']}/{boss['max_health']} \nNerves: {boss['nerves']}/{boss['max_nerves']} \nAttack Potency: {boss["attack_potency"]}x")
                    input("Enter Anything to go back to main battle menu: ")
                    continue
                case 2:
                    if inventory:
                        for item in inventory:
                            print(f'{inventory.index(item)}. {item['name']}')
                            for stat in item:
                                if item[stat] == 0 or stat == 'name':
                                    continue

                                match stat:
                                    case 'health_effect':
                                        if item[stat] > 0:
                                            print(f'    Heals {item[stat]} Health')
                                        else:
                                            print(f'    Deals {item[stat] * -1} Damage')
                                    case 'nerves_effect':
                                        if item[stat] > 0:
                                            print(f'    Adds {item[stat]} Nerves')
                                        else:
                                            print(f'    Inflicts {item[stat]} Nerves')
                                    case 'health_overtime_effect':
                                        if item[stat] > 0:
                                            print(f'    Heals additional {item[stat]} health every turn for {item['duration']}')
                                        else:
                                            print(f'    Deals additional {item[stat] * -1} damage every turn for {item['duration']}')
                                    case 'nerves_overtime_effect':
                                        if item[stat] > 0:
                                            print(f'    Adds additional {item[stat]} nerves every turn for {item['duration']}')
                                        else:
                                            print(f'    Inflicts additional {item[stat]} nerves every turn for {item['duration']}')
                                    case 'to_player':
                                        if item[stat]:
                                            print('Affects: Player')
                                        if not item[stat]:
                                            print('Affects: Opponent')
                    else:
                        input("Welp, there's nothing here, back to the main battle menu. ")
                        continue

                    try:
                        TakeAction(inventory[int(input("Which item do you wish to use (Enter Number)? "))], boss['nerves'], True, boss)
                    except:
                        input("Eh-hem, you entered that incorrectly. Let's roll this back. ")
                        continue
                case 3:
                    for attack in player_attacks:
                            print(f'{player_attacks.index(attack)}. {attack['name']}')
                            for stat in attack:
                                if attack[stat] == 0 or stat == 'name':
                                    continue

                                if attack[stat] == 'damage':
                                    print(f'    Deals {attack[stat]} Damage')
                                elif attack[stat] == 'discomfort':
                                    print(f'    Inflicts {attack[stat] * -1} Nerves')

                    TakeAction(player_attacks[int(input("Which item do you wish to use (Enter Number)? "))], boss['nerves'], True, boss)
                
            turn += 1

input(game_intro)
Dialogue(["Once upon a time", 
          "There was a great nation known as the Even More United States of America, or EMUSA", 
          'The nation lived harmonously. Folks from around the nation, from the North Pole to British Texas (which you may know as "Australia") were united under a common love for peace and democracy',
          "But one day, all of that changed.",
          'A man only known as "N. Cage" stole the constitution of EMUSA, sending the country into chaos.',
          'Apparently, he meant to steal a different document, so one thing lead to another, and the 5 pages of the constitution were spread across the land.',
          'Naturally, the most powerful of the nation jumped at the opportunity for power, and stole the pages near to them',
          'You are a new intern at the White House...',
          '*T*    *W*    *O*',
          'So before you knew it, you were sent off to retrieve the pages and save EMUSA.',
          '...'
          'Who am I?',
          "I'm the voice in your head of course! I'll be guiding you on this important quest.",
          'But first, who are you?'])

name = input("Enter your name here: ")

name = input(f'Really? Are you sure "{name}" is your name? Write your name again just to be sure, or write a different name if the one you entered was wrong: ')

Dialogue([f"Well then, it's a pleasure to meet you {name}",
          "Now, let's save America!"])


while True:

    if position not in places_been:
        for boss in bosses:
            if boss["location"] == position and boss["is_defeated"] == False:
                places_been.append(position)
                Fight(boss)

    print("Here's where you can go:")
    for place in places_to_go[position]:
        print(f"{place}. {locations[place]}")
    position = Move(position, int(input("Where would you like to go? ")))

    