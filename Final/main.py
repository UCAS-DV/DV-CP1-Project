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

game_dialogue = [
    # Intro [0]
    [game_intro, "Hello", "goodbye", "sigma"]
]

inventory = []

player_stats = {
    "health": 100,
    "nerves": 100,
    "strength": 1,
    "bravery": 1,
    "durability": 1
}

player_attacks = [
    {
        "name": "Uncouth Declaration",
        "damage": 0,
        "discomfort": 10,
        "description": '''Forget physical damage! Emotional damage is where it's at!
        Reduce your enemies NERVES by saying something mean to them!''',
        "attack_super_sucess": ["Oh...", "wow...", "I get how intense this situation is but you didn't have to go that far.", "To be frank I don't even know if you can legally say that."],
        "attack_sucess": ["Oh! He's absolutely devastated!"],
        "attack_failure": ["Okay, so, pro tip...", 'Calling your opponent "Stinky" is not very effective past the first grade'],
        "attack_super_failure": ["What was that?!", "That is likely the single most tame, polite sentence ever constructed"],
        "special_effect": None
    }
]

def Dialogue(dialouge):
    for line in dialouge:
        input(line)

def IncorrectAction(action, action_type, input):
    # Action Key
    # 0 == Movement

    # Action Type Key
    # 0 == Nonexistent Command
    # 1 == Redundent Command

    if action == 0:
        if action_type == 0:
            print(f"Um, are you crazy? {input} doesn't exist. \nYou did not move.")
        else:
            print(f"Um, you're already at {input}. Congrats? \nYou did not move.")

def Move(current_local, desired_local):

    if desired_local == current_local:
        IncorrectAction(0, 1, locations[desired_local])
        return current_local
    elif locations[desired_local] not in locations:
        IncorrectAction(0, 0, [desired_local])
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

def Fight(boss):
    turn = -1

    if turn < 0:
        Dialogue(boss["intro"])
        turn += 1

    if turn % 2 == 0:
        print('''
-~-~-~-~-~Battle-~-~-~-~-~
1. Check Stats
2. Select Item
3. Select Attack''')
        


Dialogue(game_dialogue[0])

while True:
    print(position)
    position = Move(position, int(input("Where would you like to go? ")))