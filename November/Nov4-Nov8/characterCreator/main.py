# Races
race_human = {
    "name": "Human",
    "health": 100,
    "dexterity": 100,
    "intelligence": 100
}
race_elf = {
    "name": "Elf",
    "health": 75,
    "dexterity": 115,
    "intelligence": 150
}
race_orc = {
    "name": "Orc",
    "health": 150,
    "dexterity": 70,
    "intelligence": 60
}
race_microbe = {
    "name": "Literally just a Microbe",
    "health": 1,
    "dexterity": 1,
    "intelligence": 1
}
races = [race_human,race_elf,race_orc]

# Classes
class_patriot = {
    "name": "Patriot",
    "health_bonus": 75,
    "dexterity_bonus": -30,
    "intelligence_bonus": -50
}
class_outlaw = {
    "name": "Outlaw",
    "health_bonus": 10,
    "dexterity_bonus": 30,
    "intelligence_bonus": 20
}
class_embezzeler = {
    "name": "Embezzeler",
    "health_bonus": -20,
    "dexterity_bonus": -20,
    "intelligence": 60
}
classes = [class_embezzeler, class_patriot, class_outlaw]

stats = {
    "class": ""
    "race": ""
}

print("~-~-~-~-~-~-Create Your Character~-~-~-~-~-~-")

while True:
    print("Choose your race")
    for race in races:
        print(f"- {race["name"]}")
    
    player_race = input("Make your selection: ").lower()

    if player_race not in ["human", "orc", "elf", "microbe"]:
        print("Invalid Choice!")
        continue

    print("Choose your class")
    for class_choice in classes:
        print(f"- {class_choice["name"]}")
    
    player_race = input("Make your selection: ").lower()

    if player_race not in ["patriot", "outlaw", "embezzeler"]:
        print("Invalid Choice!")
        continue

    

