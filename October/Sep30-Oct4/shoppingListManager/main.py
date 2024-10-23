intro = '''-~-~-~-~-~Shopping List Manager-~-~-~-~-~
Welcome to the shopping list manager!
Enter "1" to add an item
Enter "2" to remove an item
Enter "3" to empty the list
Enter "4" to exit the program'''

shopping_list = []
item = ""

while True:  

    print(intro)
    action = input("What would you like to do? ")
    match action:
        case "1":
            item = input("What would you like to add? ")
            shopping_list.append(item)
        case "2":
            item = input("What would you like to remove? ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Sorry! That item isn't in the list! Try again...")
        case "3":
            shopping_list = []
        case "4":
            exit()
        case _:
            print("Sorry! Invalid Input. Please try again.")
            continue
    print('''--------Shopping List--------''')
    for entry in shopping_list:
        print(f"- {entry}")
        