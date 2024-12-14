import random

# Debug Values. Do not apply to game.
skip_intro = True
instawin = True
print_all_dialogue = False

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
location_dialogue = [
    ["Boss"],
    ['Welcome to Spookytown!'],
    ['Welcome to Area 51!']
]

items = [
    {
        "name": "High Hopes and Determination",
        "health_effect": 10,
        "nerves_effect": 40,
        "to_player": True,
        'use_text': ["While on the ropes, it all comes back to you in a flash.", 
"You remember who you truly are.",
"You are not someone to be defeated by mere fatal injuries.",
"This journey has reminded you that, not only you have friends and a family to come back to, but everyone in this country you've been fighting for has people to come back to as well",
"You are suddenly filled with high hopes and determination."],
        'is_item': True
    },
    {
        'name': 'Skull of Mr. Skellybones',
        'health_effect': -10,
        'nerves_effect': -40,
        'to_player': True,
        'use_text': ['Blank'],
        'is_item': True
    },
    {
        "name": "Laser Blaster!",
        "health_effect": -30,
        "nerves_effect": 0,
        "to_player": False,
        'use_text': ['Pew Pew!'],
        'is_item': True,
    }
]
location_items = [
    # Just a White Void [0] (No Item)
    {},
    # Spookyland [1] (No Item)
    {},
    # Area 51 [2]
    items[2]
]

name = 'You'
inventory = []

player_stats = {
    "health": 100,
    "nerves": 100,
    "strength": 0,
    "bravery": 0,
    "durability": 0,
    "recovery": 0,
    "max_health": 100,
    "max_nerves": 100,
    "min_nerves": 25,
    "attack_potency": 1,
    'recovery_potency': 1,
    'pages': 0
}
player_attacks = [
    {
        "name": "Uncouth Declaration",
        "description": '''Forget physical damage! Emotional damage is where it's at!''',
        "health_effect": 0,
        "nerves_effect": -15,
        'to_player': False,
        "super_success": ["Oh...", "wow...", "I get how intense this situation is but you didn't have to go that far.", "To be frank I don't even know if you can legally say that."],
        "success": ["Oh! He's absolutely devastated!"],
        "failure": ["Okay, so, pro tip...", 'Calling your opponent "Stinky" is not very effective past the first grade'],
        "super_failure": ["What was that?!", "That is likely the single most tame, polite sentence ever constructed"],
        "is_item": False
    },
    {
        "name": "School-Appropriate Attack",
        "description": '''Deal damage to your opponent in a very school appropriate way with one simple trick!''',
        "health_effect": -10,
        "nerves_effect": 0,
        'to_player': False,    
        "super_success": ['1'],
        "success": ['2'],
        "failure": ['3'],
        "super_failure": ['4'],
        "is_item": False
    },
    {
        "name": "Deep Breaths",
        "description": '''Breathe in... Breathe out... Feels better right?''',
        "health_effect": 0,
        "nerves_effect": 15,
        'to_player': True,
        "super_success": ['1'],
        "success": ['2'],
        "failure": ['3'],
        "super_failure": ['4'],
        "is_item": False
    },
]
overall_level = 0

if instawin:
    player_attacks.append({
        "name": "Falcon Punch",
        "description": '''Insta-Kill for Debugging''',
        "health_effect": -1000,
        "nerves_effect": -1000,
        'to_player': False,
        "super_success": ['The Debugging is Debugging Greatly'],
        "success": ['The Debugging is Debugging'],
        "failure": ['The Debugging is Kinda Debugging'],
        "super_failure": ['The Debugging is Not Debugging'],
        "is_item": False
    })

boss_attacks = [
    # The Voice in Your Head
    [
        {
            "name": "Terrible Pessimism",
            "health_effect": 0,
            "nerves_effect": -15,
            "to_player": True,
            "super_success": ['1'],
            "success": ['2'],
            "failure": ['3'],
            "super_failure": ['4']
        },
        {
            "name": "Pep Talk",
            "health_effect": 10,
            "nerves_effect": 0,
            "to_player": False,
            "super_success": ['1'],
            "success": ['2'],
            "failure": ['3'],
            "super_failure": ['4']
        },
        {
            "name": "Unbearable Yell",
            "health_effect": -10,
            "nerves_effect": -5,
            "to_player": True,
            "super_success": ['1'],
            "success": ['2'],
            "failure": ['3'],
            "super_failure": ['4']
        },
        {
            "name": "Positive Affirmations",
            "health_effect": 0,
            "nerves_effect": 10,
            "to_player": False,
            "super_success": ['1'],
            "success": ['2'],
            "failure": ['3'],
            "super_failure": ['4']
        }
    ],
    # Mr. Skellybones
    [
        {
            "name": "Funny Bone Blow",
            "health_effect": -10,
            "nerves_effect": -5,
            "to_player": True,
            "super_success": ["With what you think is a deadpan expression", "(you can't really tell because he's just a faceless skeleton)", 
                              "He lightly taps your funny bone.", "You look at him confused but suddenly... what feels like a jolt of lightening traverses through your arm and-",
                              '...', '...', 'You good?', 'It seems like your brain was too focused on writhing in very unfunny pain to remember to conjure my existence.', "Uh, don't do that again.",
                              "It's kind of a buzzkill."],
            "success": ['He hits your funny bone in a very unfunny way'],
            "failure": ['He tries to hit your funny bone in a very unfunny way but he only lightly taps it'],
            "super_failure": ['He tries to hit your funny bone but he trips and hits his own funny bone.', 'He lays on the ground immobilized as you look down at him with pity.',
                              '"THIS IS NOT FUNNY RAAAAAAH"', 'Eventually he gets his footing and the battle continues.']
        },
        {
            "name": "Disturbing Truth",
            "health_effect": 0,
            "nerves_effect": -15,
            "to_player": True,
            "super_success": ['He walks up to you and whispers to you...', '"Raaaah."', '[My lawyer has advised me to remove the following dialogue]'],
            "success": ['"Raaaah. 2017 was 7 years ago."', 'You feel disturbed.'],
            "failure": ['"Raaaah. Some people are poor."', 'You feel a little bummed out.'],
            "super_failure": ['Mr. Skellybones tries to disturb you but it ended up being such a blatant truth that you feel nothing.', 'You look at him with a deadpan expression.', 
                              'He feels a little embarressed.']
        },
        {
            "name": "Got Milk?",
            "health_effect": 20,
            "nerves_effect": 0,
            "to_player": False,
            "super_success": ['He reaches behinda grave and grabs a jug of Kirkland milk.', '"Raaaah. Only Kirkland Milk makes feel this good."', 
            '"You can find Kirkland Milk at your local Costco for only $4.29"', 'He tilts his skull in what you think is a wink and drinks the whole cartoon.', 
            'He looks significantly more health y.'],
            "success": ['He reaches behind a grave and grabs a jug of Great Value(TM) milk.', 'He drinks it and looks revitalized.'],
            "failure": ['He reaches behind a grave and grabs a jug of expired Great Value(TM) milk.', "He drinks it and seems disgusted, you can't tell because he's just a skeleton."],
            "super_failure": ['He reaches behind a grave and grabs an empty jug of Kirkland milk.', 'He looks at the jug with despair.', '"Raaaah. Why did you have to leave me too dear Kirkland Milk"',
            'You reconcile him as he despairs', '"Raaaah. Thank you"', "Now that he's feeling better, you hug and then continue the fight"]
        },
    ]
]
bosses = [
    {
        "name": "The Voice In Your Head",
        "health": 50,
        "nerves": 100,
        "max_health": 100,
        "max_nerves": 100,
        "min_nerves": 25,
        "attack_potency": 1,
        "victory_item": items[0],
        "location": 0,
        'index': 0,
        "intro": ["Battle GO!"],
        "boss_victory_text": ["Oh!", "How did you...", "I don't even exist!", "Wait, if you're gone, and I'm in your head, what does that mean for me?", "...", "Uh oh."],
        "boss_defeat_text": ["Wow! Bravo! Now that you know how to battle, it seems like you're ready to save the country and retrieve the pages!", 
                             "And don't worry, since I don't exist, I'm completely fine!", 
                             "I'll never leave..."],
        "is_defeated": False,
        'encountered': False
    },
    {
        "name": "Mr. Skellybones",
        "health": 80 + (20 * overall_level),
        "nerves": 100,
        "max_health": 100,
        "max_nerves": 100,
        "min_nerves": 25,
        "attack_potency": 1,
        "victory_item": items[1],
        "location": 1,
        'index': 1,
        "intro": ["As you traverse the spookyland, you can feel chills go down your spine", "You've always heard tales about the scariness of spookyland but you never believed it",
                  'I mean, back in grade school folks would say that spookyland was ruled by a living skeleton called Mr. Skellybones.', 'How absurd...', 
                  'How could you tell it is a "Mr." if it is just bones?', "It just doesn't make sense", 'Anyway, you cautiously traverse the dark and cool landsc-',
                  '"RAAHHHHHHHHHHHHHH!"', '"IT IS I, MR. SKELLYBONES AND..."', '"I AM A MAN"', '"RAHHHHHHHHHHHHH!"', 
                  "AAAAA!", "You quiver in fear, hoping to pass through peacefully. Hopefully this detour will end so we can go back to getting the pa-", 
                  'You see a piece of parchment in his hand.', 'Uh oh...'],
        "boss_victory_text": ['Hi'],
        "boss_defeat_text": ["Wow! Bravo! Now that you know how to battle, it seems like you're ready to save the country and retrieve the pages!", 
                             "And don't worry, since I don't exist, I'm completely fine!", 
                             "I'll never leave..."],
        "is_defeated": False,
        'encountered': False
    }
]

def Dialogue(dialogue):
    if not print_all_dialogue:
        for line in dialogue:
            input(f'{line} ({dialogue.index(line) + 1}/{len(dialogue)})')
    else:
        for line in dialogue:
            print(f'{line} ({dialogue.index(line) + 1}/{len(dialogue)})')
        else:
            print('Enter anything to continue')
      
def ShowOptions(choices, selection_prompt, display_only):
    input_taken = False
    player_choice = 0
    
    while not input_taken:
        for choice in choices:

            # Checks if the choice has an health_effesct because only items and attacks have them, so this is to check if the choice is an attack or item
            if type(choice) is dict:

                print(f'{choices.index(choice)}. {choice['name']}')

                for stat in choice:
                    if choice[stat] == 0 or stat == 'name':
                        continue

                    match stat:
                        case 'description':
                            print(f'    - {choice[stat]}')
                        case 'health_effect':
                            if choice[stat] > 0:
                                print(f'    - Heals {choice[stat]} Health')
                            else:
                                print(f'    - Deals {choice[stat] * -1} Damage')
                        case 'nerves_effect':
                            if choice[stat] > 0:
                                print(f'    - Adds {choice[stat]} Nerves')
                            else:
                                print(f'    - Inflicts {choice[stat]} Nerves')
                        case 'health_overtime_effect':
                            if choice[stat] > 0:
                                print(f'    - Heals additional {choice[stat]} health every turn for {choice['duration']} turns')
                            else:
                                print(f'    - Deals additional {choice[stat]} damage every turn for {choice['duration']} turns')
                        case 'nerves_overtime_effect':
                            if choice[stat] > 0:
                                print(f'    - Adds additional {choice[stat]} nerves every turn for {choice['duration']} turns')
                            else:
                                print(f'    - Inflicts additional {choice[stat]} nerves every turn for {choice['duration']}')

                if choice['to_player'] == True:
                    print('    - Affects: Player')
                if choice['to_player'] == False:
                    print('    - Affects: Opponent')
            else:
                print(f'{choices.index(choice)}. {choice}')

        if not display_only:    
            try:
                player_choice = int(input(selection_prompt))
            except:
                print("Oops! Seems like you inputted something wrong. Let's roll that back.")
                continue

            if player_choice < 0 or player_choice > (len(choices) - 1):
                return -1
        
        return player_choice
       
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

def RollNerveEffect(nerves):
    rolled_number = random.randint(1,100)

    if rolled_number > nerves:
        if rolled_number > (nerves * 1.75):
            return 0
        else:
            return 0.5
    else:
        if rolled_number < (nerves * 0.1):
            return 1.5
        else:
            return 1  

def TakeAction(action, nerves_value, from_player, boss):
    nerve_multipler = RollNerveEffect(nerves_value)
    effectiveness = ['I do not know the effectiveness of this action']
    user_text = [f'I do not know who did this action']

    if from_player:
        user_text = [f'You used {action['name']}!']
    else:
        user_text = [f'{boss['name']} used {action['name']}!']

    health_effect = 0
    nerves_effect = 0

    if not from_player or not action['is_item']: 
        match nerve_multipler:
            case 0:
                effectiveness = ['Action was a complete failure.']
                Dialogue(user_text + action['super_failure'] + effectiveness)
            case 0.5:
                effectiveness = ['Action was a ineffective.']
                Dialogue(user_text + action['failure'] + effectiveness)         
            case 1:
                effectiveness = ['Action was a success!']
                Dialogue(user_text + action['success'] + effectiveness)
            case 1.5:
                effectiveness = ['Action was super effective!']
                Dialogue(user_text + action['super_success'] + effectiveness)
    else:
        Dialogue(action['use_text'])
    
       
    # Verifies whether the attack came from the player or boss
    if from_player and not action['is_item']:
        health_effect = action['health_effect'] * nerve_multipler
        nerves_effect = action['nerves_effect'] * nerve_multipler

        if action['to_player']:
            player_stats['health'] += health_effect * player_stats['recovery_potency']
            player_stats['nerves'] += nerves_effect * player_stats['recovery_potency']
        
            print(f'You healed {health_effect} health.')
            print(f'You gained {nerves_effect} nerves.')
        else:
            boss['health'] += health_effect * player_stats['attack_potency']
            boss['nerves'] += nerves_effect * player_stats['attack_potency']

            print(f'You dealt {health_effect * -1} damage.')
            print(f'{boss['name']} lost {nerves_effect * -1} nerves.')  

    elif from_player and action['is_item']:

        health_effect = action['health_effect'] 
        nerves_effect = action['nerves_effect']

        Dialogue(user_text)

        if action['to_player']:
            player_stats['health'] += health_effect
            player_stats['nerves'] += nerves_effect
        
            print(f'You healed {health_effect} health.')
            print(f'You gained {nerves_effect} nerves.')
        else:
            boss['health'] += health_effect
            boss['nerves'] += nerves_effect

            print(f'You dealt {health_effect * -1} damage.')
            print(f'{boss['name']} lost {nerves_effect * -1} nerves.')  
        inventory.pop(inventory.index(action))
    # If the action was not from a player, it will be handled as an item and use the boss's pool of attacks
    else:
        health_effect = action['health_effect'] * (nerve_multipler + (0.1 * overall_level))
        nerves_effect = action['nerves_effect'] * (nerve_multipler + (0.1 * overall_level))

        if action['to_player']:
            player_stats['health'] += health_effect
            player_stats['nerves'] += nerves_effect

            print(f'{boss['name']} dealt {health_effect * -1} damage to you.')
            print(f'You lost {nerves_effect * -1} nerves.')     
        else:
            boss['health'] += health_effect
            boss['nerves'] += nerves_effect
            print(f'{boss['name']} healed {health_effect} health.')
            print(f'{boss['name']} gained {nerves_effect} nerves.')

    if player_stats['health'] > player_stats['max_health']: player_stats['health'] = player_stats['max_health'] 

    if player_stats['nerves'] > player_stats['max_nerves']: player_stats['nerves'] = player_stats['max_nerves']
    elif player_stats['nerves'] < player_stats['min_nerves']: player_stats['nerves'] = player_stats["min_nerves"] 

    if boss['health'] > boss['max_health']: boss['health'] = boss['max_health']
       
    if boss['nerves'] > boss['max_nerves']: boss['nerves'] = boss['max_nerves']
    elif boss['nerves'] < boss['min_nerves']: boss['nerves'] = boss["min_nerves"] 

def Fight(boss, level):
    turn = -1
    fight_finished = False
    player_action = {}

    boss['encountered'] = True

    while not fight_finished:

        if turn < 0:
            Dialogue(boss["intro"])
            turn += 1
        elif turn % 2 == 0:
            print(f'-~-~-~-~-~{boss["name"]}-~-~-~-~-~ )')
            try:
                action = ShowOptions(['Check Stats', 'Select Item', 'Select Attack'], 'What is your choice? ', False)
            except:
                print("Seems like you entered that incorrectly. Let's roll this back. ")
                continue

            match action:
                case 0:
                    print(f"-=-=-=-{name}'s Stats-=-=-=-")
                    print(f"Health: {player_stats["health"]}/{player_stats["max_health"]} \nNerves: {player_stats["nerves"]}/{player_stats["max_nerves"]} \nAttack Potency: {player_stats["attack_potency"]}x")
                    print(f"Minimum Nerves: {player_stats['min_nerves']} \nDurability: {player_stats['durability']} \nBravery: {player_stats["bravery"]} \nStrength: {player_stats["strength"]}")
                    print(f"-=-=-=-{boss['name']}'s Stats-=-=-=-")
                    print(f"Health: {boss['health']}/{boss['max_health']} \nNerves: {boss['nerves']}/{boss['max_nerves']} \nMinimum Nerves: {boss['min_nerves']}\nAttack Potency: {boss["attack_potency"]}x")
                    input("Enter Anything to go back to main battle menu: ")
                    continue
                case 1:
                    if not inventory:
                        input("Welp, there's nothing here, back to the main battle menu. ")
                        continue
                    player_action = ShowOptions(inventory, "Which item do you wish to use (Enter Number)? ", False)

                    if player_action < 0:
                        continue

                    TakeAction(inventory[player_action], player_stats['nerves'], True, boss)
                case 2:        
                    player_action = ShowOptions(player_attacks, "Which attack do you wish to use (Enter Number)? ", False)

                    if player_action < 0:
                        continue

                    TakeAction(player_attacks[player_action], player_stats['nerves'], True, boss)        
                
            input(f"-+-+-+-+-{boss['name']}'s Turn-+-+-+-+-")  
            turn += 1  
        else:
            boss_attack = {}
            rerolls = 0
            boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]

            # Following If Statements are to ensure the boss doesn't make any redundant moves
            if boss_attack['health_effect'] > 0 and boss['health'] == boss['max_health']:
                boss_attack =  boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]

            if boss_attack['nerves_effect'] > 0 and boss['nerves'] == boss['max_nerves']:
                boss_attack =  boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
            
            if rerolls < 3:
                if player_action["nerves_effect"] < 0 and not player_action['to_player'] and boss_attack['nerves_effect'] <= 0:
                    boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                    rerolls += 1

            TakeAction(boss_attack, boss['nerves'], False, boss)
            input(f"-+-+-+-+-{name}'s Turn-+-+-+-+-")
            turn += 1
        
        # Game Over Sequence
        if player_stats['health'] <= 0:
            player_stats["health"] = player_stats['max_health']
            player_stats['nerves'] = player_stats['max_nerves']
            Dialogue(boss['boss_victory_text'])
            places_been.pop()
            position = 0
            fight_finished = True
        
        # Victory Sequence
        elif boss['health'] <= 0:
            Dialogue(boss['boss_defeat_text'])

            # Give Player Reward Item
            inventory.append(boss['victory_item'])
            input('You have a new item! (1/1)')
            input(ShowOptions([boss['victory_item']], 'Test', display_only=True))

            # Have player choose what stat to level up
            match ShowOptions([f'Strength: {player_stats["strength"]}', f'Bravery: {player_stats['bravery']}', f'Durability: {player_stats['durability']}', f'Recovery: {player_stats['recovery']}'], 'Which stat do you wish to level up? ', False):
                case 0:
                    player_stats['strength'] += 1
                    player_stats['attack_potency'] += (player_stats["strength"]) * 0.1
                    Dialogue([f'Your strength is now at Level {player_stats['strength']}!'])
                case 2:
                    player_stats['durability'] += 1
                    player_stats['max_health'] += (player_stats['durability']) * 15
                    Dialogue([f'Your durability is now at Level {player_stats['durability']}!'])
                case 1:
                    player_stats['bravery'] += 1
                    player_stats['max_nerves'] += (player_stats["bravery"]) * 5
                    player_stats['min_nerves'] += (player_stats['bravery']) * 5
                    Dialogue([f'Your durability is now at Level {player_stats['bravery']}!'])
                case 3:
                    player_stats['recovery'] += 1
                    player_stats['recovery_potency'] += (player_stats["recovery"]) * 0.1

            level += 1
            player_stats['pages'] += 1
            
            #attacks = []
    
            #for attack in boss_attacks[boss['index']]:
            #    attacks.append(attack)

            #attack_to_learn = boss_attacks[boss['index']][ShowOptions(attacks, 'Which attack would you like to learn? ', False)]
            
            #This is so the player has an empty space for attack selection
            #if boss['name'] == "The Voice In Your Head":
            #    player_attacks.append({'name': 'Empty Space', 'to_player': False})

            #attack_to_replace_index = ShowOptions(player_attacks, 'Which attack would you like to replace? ', False)

            #player_attacks[attack_to_replace_index] = attack_to_learn

            #Dialogue([f'You have learned "{attack_to_learn['name']}"'])

            # Reset Player health and nerves and mark boss as defeated
            player_stats["health"] = player_stats['max_health']
            player_stats['nerves'] = player_stats['max_nerves']
            boss['is_defeated'] = True
            fight_finished = True

if not skip_intro:
    input(game_intro)
    Dialogue(["Once upon a time,", 
          "There was a great nation known as the Even More United States of America, or EMUSA.", 
          'The nation lived harmonously. Folks from around the nation, from the North Pole to British Texas (which you may know as "Australia") were united under a common love for peace and democracy',
          "But one day, all of that changed.",
          'A man only known as "N. Cage" stole the constitution of EMUSA, sending the country into chaos.',
          'Apparently, he meant to steal a different document, so one thing lead to another, and the 5 pages of the constitution were spread across the land.',
          'Naturally, the most powerful of the nation jumped at the opportunity for power, and stole the pages near to them',
          'You are a new intern at the White House.',
          'So before you knew it, you were sent off to retrieve the pages and save EMUSA.',
          '...',
          'Who am I?',
          "I'm the voice in your head of course! I'll be guiding you on this important quest.",
          'But first, who are you?'])

    name = input("Enter your name here: ")

    name = input(f'Really? Are you sure "{name}" is your name? Write your name again just to be sure, or write a different name if the one you entered was wrong: ')

    Dialogue([f"Well then, it's a pleasure to meet you {name}.",
          "Now, let's save America!"])

while True:

    if position not in places_been:
        places_been.append(position)
        for boss in bosses:
            if boss["location"] == position and boss["is_defeated"] == False:
                Fight(boss, overall_level)
                break
        else:
            inventory.append(location_items[position])
            input('You have a new item! (1/1)')
            ShowOptions([location_items[position]], 'Test', display_only=True)
            input('Press anything to continue')

    match ShowOptions(['Move', 'Stats', 'Inventory', 'Attacks'], 'What would you like to do? ', False):
        case 0:
            try:
                print(f"Since you're currently at {locations[position]}, you can go to: ")
                for place in places_to_go[position]:
                    print(f"{place}. {locations[place]}")
                position = Move(position, int(input("Where would you like to go? ")))
            except:
                print("Oops! Seems like you entered something incorrectly. Let's try that again")
        case 1:
            print(f"-=-=-=-{name}'s Stats-=-=-=-")
            print(f"Health: {player_stats["health"]}/{player_stats["max_health"]} \nNerves: {player_stats["nerves"]}/{player_stats["max_nerves"]} \nAttack Potency: {player_stats["attack_potency"]}x")
            print(f"Minimum Nerves: {player_stats['min_nerves']} \nStrength: {player_stats["strength"]} \nBravery: {player_stats["bravery"]} \nDurability: {player_stats['durability']} \nRecovery: {player_stats['recovery']}")
            input('Type anything to go back. ')
        case 2:
            ShowOptions(inventory, "Which item do you wish to use (Enter Number)? ", True)
            input('Enter anything to go back. ')
        case 3:
            ShowOptions(player_attacks, '', True)
            input('Enter anything to go back. ')
    