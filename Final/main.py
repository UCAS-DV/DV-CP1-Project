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


inventory = []

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
        IncorrectAction(0, 0, locations[desired_local])
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
        
input(game_intro)


while True:

    print(position)
    position = Move(position, int(input("Where would you like to go comrade? ")))