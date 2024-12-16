import random

# Debug Values. Do not apply to game.
skip_intro = False
debug_attacks = True
print_all_dialogue = True

game_title_screen = '''
-~-~-~-~-~-~Quest for the Country!-~-~-~-~-~-~
           Enter Anything to Start
                      '''

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
    ["Boss"],
    ['Due to some unfortunate events, the government was running low on cash so they opened Area 51 to the public for tourism.', 
    'Of course, you have to sign a massive waiver to get in because of the crazy stuff happening.', 
    'For example, just last week they were testing to see if radiation from nuclear fission could be used for cereal production and they used tourists to test the quality of the cereal.',
    '...', "I'm just kidding of course.", "They don't have you sign a waiver.", 
    "Anyway, Area 51 has been effectively abandoned because apparently government facilities aren't too useful without the government.",
    'So you shrug and aimlessly wander the facility, trying to find a page but when digging around a bin with the label "Biohazard", you hear a familiar voice', '"Veep bloop glorb?"',
    "That's right, it's your childhood friend and your neighborhood's resident alien, Zeep Vorp!", '"Vlam yoop blam zeep."', '"Yeem glob tram!"', 
    "You laugh hysterically. Seems like Zeep hasn't lost his wit!", '"Yam uup glep?"', "You show him a page of the constitution and he suddenly realizes what you're doing.", 
    '"Zeee, hep jam"', 'He hands you a laser pistol, although it seems that he accidentally left a proton charge on the trigger. Classic Zeep Vorp!', 'You remove the charge, bow in gratitude, and go on your way!', '"Verplum!"'
    ],
    ['Out of boredom, you read through a page of the constitution you have and on it you notice that it mentions how the government should treat North Dakota.', 'Wait...', 
    'North Dakota?!', "There's no way...", 
    'Apparently the mythical state of North Dakota is not as mythical as commonly thought.', "Maybe the state is real but the sky cities and robot dogs and magic isn't real",
    "Well, there's no harm in checking for pages there.", "So, before you know it, you're dining with the king of North Dakota in a city 1000 meters up, levitated with magic.",
    'This is... odd, to say the least.', 'Anyways, you show the king your page and he explains he has not seen anything like it so after you finish eating you decide to go on your way',
    'He hands you a slab of "Northdakotium" and wishes you safe travels.', 
    "He forgot to explain to you what it does, assuming that you already know, so you don't really know what to do with it", "It's a nice gift so you're still happy."]
]

player_stats = {
    'name': 'You',
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
    'pages': 0,
    'level': 0,
    'position': 0
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

items = [
    {
        "name": "High Hopes and Determination",
        'description': "Well, this isn't quite what you signed up for but your main character syndrome stops you from letting your country fall.",
        "health_effect": 30,
        "nerves_effect": 30,
        "to_player": True,
        'use_text': ["While on the ropes, it all comes back to you in a flash.", 
"You remember who you truly are.",
"You are not someone to be defeated by mere fatal injuries.",
"This journey has reminded you that, not only you have friends and a family to come back to, but everyone in this country you've been fighting for has people to come back to as well.",
"You are suddenly filled with high hopes and determination."],
        'is_item': True
    },
    {
        'name': 'Skull of Mr. Skellybones',
        'description': f'"Raaah. Thank you {player_stats['name']}. Let us save our country. For Spookyland!"',
        'health_effect': -10,
        'nerves_effect': -40,
        'to_player': False,
        'use_text': ['You pull out the skull of Mr. Skellybones.', '"RAAAAAAAAHHHHHHHH! I AM MR. SKELLYBONES AND I AM A MAN!"', 
        '"I HAVE COME TO TELL YOU THAT ALL OF YOUR CELLS ARE REPLACED EVERY 7-10 YEARS!"'
        "You're opponent sits down in complete terror as they contemplate the implications of that fact.", 
        'As they start muttering to themselves about the Ship of Theseus, Mr. Skellybones tells you, "I am sorry, that is all I can muster without any milk to fuel me."', 
        'Well, given how shaken your opponent is, maybe you did make the right call bringing him along.', f'Great job {player_stats['name']}!'],
        'is_item': True
    },
    {
        "name": "Laser Blaster",
        'description': 'A state of the art plasma pistol designed by the best of Vorlom and made in China!',
        "health_effect": -50,
        "nerves_effect": 0,
        "to_player": False,
        'use_text': ['"Pew Pew!"', 'A flurry of deep blue rays of plasma cover your opponent.', 
        "As your opponent panics as to what to do, you try to fire several more shots but it seems its jammed", 'You look down at the display on the gun. It reads:',
        '"You have reached the limit for free shots from this weapon. If you wish to fire more, join Laser Premium for $8.99 a week."', 'Gross...', 
        'You shrug and chuck the blaster at your opponent.', 'It lands and they reel from the collision. They place an icepack on their head and the battle continues.'],
        'is_item': True,
    },
    {
        "name": "Slab of Northdakotium",
        'description': "You're not quite sure what to do with it but it's a nice gift.",
        "health_effect": 50,
        "nerves_effect": 0,
        "to_player": True,
        'use_text': ['In despiration, you pull out your slab of Northdakotium.', "You then pause as you realize you don't really know what to do with it.", 
        'You shrug and take a bite out of it for some reason?', 'Why was that the first thing that you thought to do?', 
        'Anyway, after taking a bite out of a literal block of metal, you suddenly feel siginficantly healthier for some reason?', 'Huh.', 'That should not have worked but what works, works, I guess.'],
        'is_item': True,
    },
    {
        "name": "Pretentious Monocle",
        'description': "Does anyone still where these things?",
        "health_effect": 0,
        "nerves_effect": 60,
        "to_player": True,
        'use_text': [''],
        'is_item': True,
    }
]
location_items = [
    # Just a White Void [0] (No Item)
    {},
    # Spookyland [1] (No Item)
    {},
    # Area 51 [2]
    items[2],
    # North Dakote [3]
    items[3]
]

inventory = []

if debug_attacks:
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
    player_attacks.append({
        'name': 'Resign',
        'description': 'Instant Game Over for Debugging',
        "health_effect": -1000,
        "nerves_effect": -1000,
        'to_player': True,
        "super_success": ['The Debugging is Debugging Greatly'],
        "success": ['The Debugging is Debugging'],
        "failure": ['The Debugging is Kinda Debugging'],
        "super_failure": ['The Debugging is Not Debugging'],
        "is_item": False
    })

reward_attacks = [
    {
        "name": "Pep Talk",
        'description': 'No pain can beat out the power of a good pep talk!',
        "health_effect": 10,
        "nerves_effect": 0,
        "to_player": True,
        "super_success": ['You give such an incredible, rousing self pep talk that even your enemy feel a little inspired.'],
        "success": ['You give yourself a pep talk and feel inspired by your own words.'],
        "failure": ['You try to give yourself a pep talk but you suck at public speaking so it proves ineffective,', "even though the only person it's directed to is yourself."],
        "super_failure": ['...', "That was...", 'something.', "Don't beat yourself up about it,", 'just ensure that you will never have to do any sort of public speaking...', 'ever...'
        "and you'll be fine!"]
    },
    {
        "name": "Funny Bone Blow",
        "health_effect": -15,
        "nerves_effect": 0,
        "to_player": True,
        "super_success": ["You look at your opponent with a deadpan expression", 'You walk up to your opponent, menacingly and your mere aura brings them to your knees.',
        "You lightly taps their funny bone.", "He looks at you confused but suddenly... what feels like a jolt of lightening traverses through their arm and you can infer the rest"],
        "success": ['You hits their funny bone in a very unfunny way'],
        "failure": ['You try to hit their funny bone in a very unfunny way but you only lightly tap it'],
        "super_failure": ["You try to hit your enemy's funny bone but you miss terribly.", 
        'You fall to the ground from the missed swing and you contemplate why you were even bothering with this quest.',
        'Your opponent pities you and encourages you to get back into the fight.', 'Eventually, the fight continues.']
    },
]
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
            "super_success": ['I give myself such an incredible, rousing self pep talk that even you feel a little inspired.', 'Wow, I should really pursue public speaking!',
            "You know, I think I might do so!", 'Yeah...', 'wait, the only person who can hear me is you.', '...', 'Ow.'],
            "success": ['I give myself a pep talk and feel inspired by my own words.'],
            "failure": ["You know...", 'I am so happy that the only person who can hear me is you.'],
            "super_failure": ['Um...', "I thought I would be better at speaking given that it's the only thing I can do.", 'Just...', 'please forget everything I just said.']
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
            "health_effect": -15,
            "nerves_effect": 0,
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
            "super_success": ['He reaches behinda grave and grabs a jug of Clarkplace(TM) milk.', '"Raaaah. Only Clarkplace Milk(TM) makes feel this good."', 
            '"You can find Clarkplace Milk(TM) at your local PriceCo(TM) for only $4.29"', 'He tilts his skull in what you think is a wink and drinks the whole cartoon.', 
            'He looks significantly more health y.'],
            "success": ['He reaches behind a grave and grabs a jug of Awesome Price(TM) milk.', 'He drinks it and looks revitalized.'],
            "failure": ['He reaches behind a grave and grabs a jug of expired Awesome Price(TM) milk.', "He drinks it and seems disgusted, you can't tell because he's just a skeleton."],
            "super_failure": ['He reaches behind a grave and grabs an empty jug of Clarkplace milk.', 'He looks at the jug with despair.', '"Raaaah. Why did you have to leave me too dear Kirkland Milk"',
            'You reconcile him as he despairs', '"Raaaah. Thank you"', "Now that he's feeling better, you hug and then continue the fight"]
        },
    ]
]
bosses = [
    {
        "name": "The Voice In Your Head",
        "health": 50,
        "nerves": 100,
        "max_health": 50,
        "max_nerves": 100,
        "min_nerves": 25,
        "victory_item": items[0],
        "location": 0,
        'index': 0,
        "intro": ["...", 'Wait a second...', "You don't know how to fight, do you?", "Well, these guys are not going to willing give up their pages so let's learn.",
        "I'm sure you're already familiar with how health works, but people often underestimate how important it is to keep a cool head.", 
        "You see, if you let your nerves get too low, you're attacks' effectiveness will likely be greatly reduced, or worse, they'll completely fail.",
        "If you keep cool and have high nerves, you're attacks won't only be likely to land properly, they may even be more powerful.", 
        'The same goes for your enemies. So make sure to maintain high nerves for yourself, and reduce their nerves.', 
        "Don't worry if you get too nervous, you will likely have items you collect from bosses or location that you can use as hail marys, regardless of your nerves.", 
        "Although, you can only use them once so be conservative with your item use.",
        "Also, if things get too bad, there's a minimum value your nerves can fall under. Although sadly, your enemies also have a minimum nerves value.",
        "Now that we have that settled, let's begin! I'll be your first boss so you can apply your new knowledge.", 
        'By the way, to traverse menus, you must enter the numbers of the options and if you enter a menu you wish to exit, type anything but the selected options.'],

        "boss_victory_text": ["Oh!", "How did you...", "I don't even exist!", "Wait, if you're gone, and I'm in your head, what does that mean for me?", "...", "Uh oh."],

        "boss_defeat_text": ["Wow! Bravo! Now that you know how to battle, it seems like you're ready to save the country and retrieve the pages!", 
                             "And don't worry, since I don't exist, I'm completely fine!", "I'll never leave...", 
                             "Anyways, now that you've defeated me, you will get my item and be given the opportunity to upgrade one of your stats.", 'You have 4 stats:',
                             'Strength, which increases the power of your offensive attacks,', 'Bravery, which increases your maximum and minimum amount of nerves,',
                             'Durability, which increase your maximum health,', 'And Recovery, which increase the power of attacks that boost you.', 
                             'Also, you will pick up attacks from your opponents and you can learn one of them if you want', "But you're brain isn't limitless, so you'll have to forget an attack to make up for it.",
                             'Keep that in mind when deciding whehter or not you want to learn their attack.',
                             "Anyway, usually you will get a page from defeated bosses but I don't have any pages to give-",
                             "You look down at your feet to see you're standing on a page of the constitution.", "Well that's convienient."],

        "is_defeated": False,
        'encountered': False
    },
    {
        "name": "Mr. Skellybones",
        "health": 60,
        "nerves": 100,
        "max_health": 80,
        "max_nerves": 100,
        "min_nerves": 25,
        "victory_item": items[1],
        "location": 1,
        'index': 1,

        "intro": ["As you traverse the spookyland, you can feel chills go down your spine", 'As you go, you see a variety of ghouls, ghosts, zombies, and skeletons living their lives.'
                  "You've always heard tales about the scariness of spookyland but you never believed it",
                  'I mean, back in grade school folks would say that spookyland was ruled by a living skeleton called Mr. Skellybones.', 'How absurd...', 
                  'How could you tell it is a "Mr." if it is just bones?', "It just doesn't make sense", 'Anyway, you cautiously traverse the dark and cool landsc-',
                  '"RAAHHHHHHHHHHHHHH!"', '"IT IS I, MR. SKELLYBONES AND..."', '"I AM A MAN"', '"RAHHHHHHHHHHHHH!"', 
                  "AAAAA!", "You quiver in fear, hoping to pass through peacefully. Hopefully this detour will end so we can go back to getting the pa-", 
                  'You see a piece of parchment in his hand.', 'Uh oh...'],

        "boss_victory_text": ['"Raaaah. No one can withstand Mr. Skellybones!"', 'Hint: Skellybones thrives off of your fear, so keep cool and give him a taste of his own medicine.'],

        "boss_defeat_text": ['The skeleton looks up at you and suddenly collapses.', 'His bones are everywhere.', '"Raaaah, you have defeated me. What do you wish to do with me?"',
        'You walk to his hand and grab the page of the constitution and you begin to walk away.', 
        '"Raaaah. I see. Spookyland has been long neglected these days. We have not been as scary as we used to since my father retired"', 
        '"Raaaah. I hoped that I could hold the government hostage, so that they would support my people and I."', "Just a reminder, you have the page now, you can go now.",
        '"Raaaah. You have no reason to fulfill any request from me, but I ask for my people, please do not let us fall into the shadows"', 'Well, that sucks for him, you walk away and-', 
        'What are you doing?', 'You nod and gently pat him on the head.', '"Raaaah. Thank you. If you are truly dedicated to saving Spookyland, wherever you go, take me with you and I will assist you as best as I can."', 
        "You ignore the skeleton who was attacking you just 5 minutes ago because that's the normal thing to-",
        'Are you serious?', 'You pick up his skull and nod again.', '"Raaaah. Tell me, what is your name, honorable one"',
        'Well, fine then, I guess he may be useful in battle.'],

        "is_defeated": False,
        'encountered': False
    },
    {
        "name": "A Personification of Capitalism",
        "health": 50,
        "nerves": 50,
        "max_health": 120,
        "max_nerves": 120,
        "min_nerves": 15,
        "victory_item": items[2],
        "location": 5,
        'index': 2,

        "intro": ['Welcome to Town City, your home town.', "Why isn't it great to be home!", 'Air: Polluted', "Tap Water: Don't Drink", 'Crime: Of Course', 'Labor Rights: Ignored', "Truly lovely isn't it?",
        "Although, given how big this city is, if there's a page here, there's no way that we could find it anytime soon.", "Well then, let's go searching.", 
        'You traverse all throughout the city, going down a pleasant trip on Memory Lane.', 'As you peacefully go around, you notice a black limousine go through the street.', 
        'It quite literally stretches all of the way down to the horizon.', 'As you ponder who such a car would turn, you see well dressed gentleman exit right behind the front of the vehicle.', 
        'In his hand, a piece of parchment.', 'He looks back at you and fear glistens in his eyes.', 'You have garnered quite a reputation after your previous victories.', '"Henchmen, get him!"', 
        'They stand still and after you do a backflip to assert dominance, they scurry off.', '"Imbeciles! You! I will let you know that any attempt to take this page is futile."',
        '"Get any closer and I will strike you down like I strike down unions!"', 'Ah...', 'I see...', "Seems like you're fighting..."],

        "boss_victory_text": ['"You look just as hopeless as my employees after 15 hours of mandatory labor on Christmas. Hehehehe"', 'Hint: The Personification of Capitalism starts off extremely weak. Try to keep him from buffing himself'],

        "boss_defeat_text": ['"What?!"', '"No!"', '"This can not be!"', '"How dare you!"', '"I worked so hard to be the first born son of my billonare father and this is what I get! Do you not know how hard it is to dock my workers pay?!"', 
        '"I have to tell my intern to change the numbers and send out the emails!"', '"It is so tiring on my part!"', 'You shrug and grab the page out of his hand. You also take his monocle because why not?',
        '"I get it, you want to destroy me because you are too lazy to work as hard as I did to be born to a rich family!"', 'He keeps rambling as you walk away. Eventually he leaves earshot',
        'Well...', 'that was pretentious.', 'If I had eyes I would be rolling them.', "Receiving a lecture about the dangers of unfettered capitalism in a journey where you fight Santa Claus and Mr. Skellybones was odd to say the least.", 
        "Well, hey, we got a page."],

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
            input('Enter anything to continue: ')

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
    elif action['is_item']:
        Dialogue(user_text + action['use_text'])
    else:
        Dialogue(action['use_text'])
    
       
    # Verifies whether the attack came from the player or boss
    if from_player and not action['is_item']:


        if action['to_player']:

            health_effect = action['health_effect'] * nerve_multipler * player_stats['recovery_potency']
            nerves_effect = action['nerves_effect'] * nerve_multipler * player_stats['recovery_potency']

            player_stats['health'] += health_effect
            player_stats['nerves'] += nerves_effect
        
            print(f'You healed {health_effect} health.')
            print(f'You gained {nerves_effect} nerves.')
        else:

            health_effect = action['health_effect'] * nerve_multipler * player_stats['attack_potency']
            nerves_effect = action['nerves_effect'] * nerve_multipler * player_stats['attack_potency']

            boss['health'] += health_effect
            boss['nerves'] += nerves_effect

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
        health_effect = (action['health_effect'] * (nerve_multipler + (0.05 * player_stats['level'])))
        nerves_effect = (action['nerves_effect'] * (nerve_multipler + (0.05 * player_stats['level'])))

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

def Fight(boss):
    turn = -1
    fight_finished = False
    player_action = {}

    rewards_recieved = False
    stat_boosted = False
    monologue_complete = False

    saved_inventory = []
    
    boss['max_health'] += 20 * player_stats['level']
    boss['health'] = boss['max_health']

    while not fight_finished:

        if boss['health'] > 0 and player_stats['health'] > 0:
            if turn == -1:
                if not boss['encountered']:
                    Dialogue(boss["intro"])
                turn += 1
                boss['encountered'] = True
            elif turn % 2 == 0:
                input(f"-+-+-+-+-{player_stats['name']}'s Turn-+-+-+-+-")
                print(f'-~-~-~-~-~{boss["name"]}-~-~-~-~-~ ')
                try:
                    action = ShowOptions(['Check Stats', 'Select Item', 'Select Attack'], 'What is your choice? ', False)

                    if action < 0 or action > 2:
                        continue
                except:
                    print("Seems like you entered that incorrectly. Let's roll this back. ")
                    continue

                match action:
                    case 0:
                        print(f"-=-=-=-{player_stats['name']}'s Stats-=-=-=-")
                        print(f"Health: {player_stats["health"]}/{player_stats["max_health"]} \nNerves: {player_stats["nerves"]}/{player_stats["max_nerves"]} \nAttack Potency: {player_stats["attack_potency"]}x \nRecovery Potency: {player_stats['recovery_potency']}")
                        print(f"Minimum Nerves: {player_stats['min_nerves']} \nDurability: {player_stats['durability']} \nBravery: {player_stats["bravery"]} \nStrength: {player_stats["strength"]}")
                        print(f"-=-=-=-{boss['name']}'s Stats-=-=-=-")
                        print(f"Health: {boss['health']}/{boss['max_health']} \nNerves: {boss['nerves']}/{boss['max_nerves']} \nMinimum Nerves: {boss['min_nerves']}")
                        input("Enter Anything to go back to main battle menu: ")
                        continue
                    case 1:
                        if not inventory:
                            input("Welp, there's nothing here, back to the main battle menu. ")
                            continue
                        player_action = ShowOptions(inventory, "Which item do you wish to use (Enter Number)? ", False)

                        if player_action < 0:
                            continue

                        saved_inventory.append(inventory[player_action])
                        TakeAction(inventory[player_action], player_stats['nerves'], True, boss)               
                    case 2:        
                        player_action = ShowOptions(player_attacks, "Which attack do you wish to use (Enter Number)? ", False)

                        if player_action < 0:
                            continue

                        TakeAction(player_attacks[player_action], player_stats['nerves'], True, boss)        
                  
                turn += 1  
            else:

                input(f"-+-+-+-+-{boss['name']}'s Turn-+-+-+-+-")  
                boss_attack = {}
                rerolls = 0
                boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]

                # Following If Statements are to ensure the boss doesn't make any redundant moves
                if boss_attack['health_effect'] > 0 and boss['health'] == boss['max_health']:
                    boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                    continue

                if boss_attack['nerves_effect'] > 0 and boss['nerves'] == boss['max_nerves']:
                    boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                    continue
            
                if rerolls < 3:
                    if player_attacks[player_action]["nerves_effect"] < 0 and not player_attacks[player_action]['to_player'] and boss_attack['nerves_effect'] <= 0:
                        boss_attack = boss_attacks[boss['index']][random.randint(0, len(boss_attacks[boss['index']]) - 1)]
                        rerolls += 1

                TakeAction(boss_attack, boss['nerves'], False, boss)
                turn += 1
        # Game Over Sequence
        elif player_stats['health'] <= 0:
            player_stats["health"] = player_stats['max_health']
            player_stats['nerves'] = player_stats['max_nerves']
            if boss['name'] != "A Personification of Capitalism":
                boss['health'] = boss['max_health']
                boss['nerves'] = boss['max_nerves']
            else:
                boss['health'] = 50
                boss['nerves'] = 50
            Dialogue(['-!-!-!-GAME OVER-!-!-!-'] + boss['boss_victory_text'] + ["Let's run that back..."])
            if player_stats['position'] == 0:
                turn = -1
                continue
            player_stats['position'] = 0
            for saved_item in saved_inventory:
                inventory.append(saved_item)            
            fight_finished = True
        # Victory Sequence
        elif boss['health'] <= 0:

            input(player_stats['name'])

            if not monologue_complete:
                Dialogue(boss['boss_defeat_text'])
                monologue_complete = True

            if rewards_recieved == False:
                
                player_stats['pages'] += 1

                Dialogue([f'You now have {player_stats['pages']}/6 pages!'])
                
                # Give Player Reward Item
                inventory.append(boss['victory_item'])
                input('You have a new item! (1/1)')
                input(ShowOptions([boss['victory_item']], 'Test', display_only=True))
                rewards_recieved = True

            if not stat_boosted:
                # Have player choose what stat to level up
                match ShowOptions([f'Strength: {player_stats["strength"]}', f'Bravery: {player_stats['bravery']}', f'Durability: {player_stats['durability']}', f'Recovery: {player_stats['recovery']}'], 'Which stat do you wish to level up? ', False):
                    case -1:
                        continue
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
                        Dialogue([f'Your bravery is now at Level {player_stats['bravery']}!'])
                    case 3:
                        player_stats['recovery'] += 1
                        player_stats['recovery_potency'] += (player_stats["recovery"]) * 0.1
                        Dialogue([f'Your recovery stat is now at Level {player_stats['recovery']}!'])
                stat_boosted = True
            
            ShowOptions([reward_attacks[boss['index']]], 'Yippee', True)

            if boss['name'] == "The Voice In Your Head":
                Dialogue([f'You have learned Pep Talk. Congratualations!'])
                player_attacks.append(reward_attacks[0])
            else:
                replace = ShowOptions(['Yes', 'No'], 'Would you like to replace any of your attacks with this one? ', False)
                if replace == 0:                
                    player_attacks[ShowOptions(player_attacks, 'Which attack would you like to replace ? ', False)] = reward_attacks[boss['index']]
                    Dialogue([f'You have learned {reward_attacks[boss['index']]['name']}!'])
                elif replace == 1:
                    Dialogue([f'You have decided not to learn {reward_attacks[boss['index']]['name']}.'])
                else:
                    continue

            player_stats['level'] += 1
            
            # Reset Player health and nerves and mark boss as defeated
            player_stats["health"] = player_stats['max_health']
            player_stats['nerves'] = player_stats['max_nerves']
            boss['is_defeated'] = True
            fight_finished = True

if not skip_intro:

    input(game_title_screen)
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
          "Now, let's save america!"])

Fight(bosses[0])

while True:

    if player_stats['position'] != 0:
        for boss in bosses:
            if boss["location"] == player_stats['position'] and not boss["is_defeated"]:
                Fight(boss)
                break
            elif boss["location"] == player_stats['position'] and boss["is_defeated"]:
                break
        else:
            if player_stats['position'] not in places_been:
                Dialogue(location_dialogue[player_stats['position']])
                places_been.append(player_stats['position'])
                inventory.append(location_items[player_stats['position']])
                input('You have a new item! (1/1)')
                ShowOptions([location_items[player_stats['position']]], 'Test', display_only=True)
                input('Press anything to continue')

    print(f'You are at {locations[player_stats['position']]}')

    match ShowOptions(['Move', 'Stats', 'Inventory', 'Attacks', 'Settings'], 'What would you like to do? ', False):
        case 0:
            try:
                print(f"Since you're currently at {locations[player_stats['position']]}, you can go to: ")
                for place in places_to_go[player_stats['position']]:
                    print(f"{place}. {locations[place]}")
                player_stats['position'] = Move(player_stats['position'], int(input("Where would you like to go? ")))
            except:
                print("Oops! Seems like you entered something incorrectly. Let's try that again")
        case 1:
            print(f"-=-=-=-{player_stats['name']}'s Stats-=-=-=-")
            print(f"Health: {player_stats["health"]}/{player_stats["max_health"]} \nNerves: {player_stats["nerves"]}/{player_stats["max_nerves"]} \nAttack Potency: {player_stats["attack_potency"]}x \nRecovery Potency: {player_stats['recovery_potency']}")
            print(f"Minimum Nerves: {player_stats['min_nerves']} \nStrength: {player_stats["strength"]} \nBravery: {player_stats["bravery"]} \nDurability: {player_stats['durability']} \nRecovery: {player_stats['recovery']}")
            print(f'Pages: {player_stats['pages']}/{player_stats['pages']}')
            input('Type anything to go back. ')
        case 2:
            ShowOptions(inventory, "Which item do you wish to use (Enter Number)? ", True)
            input('Enter anything to go back. ')
        case 3:
            ShowOptions(player_attacks, '', True)
            input('Enter anything to go back. ')
        case 4:
            print(f'0. Instant Dialogue [{print_all_dialogue}]')
            print(f'    Prints all dialogue at once instead of writing individual lines upon player input. Good if you are short on time.')

            if input('What setting would you like to modify (If none, enter anything but the numbers)? ') == '0':
                if print_all_dialogue:
                    print_all_dialogue = False
                else:
                    print_all_dialogue = True
    