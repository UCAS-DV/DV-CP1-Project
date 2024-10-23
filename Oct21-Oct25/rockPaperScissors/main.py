import random

options = [
    "rock",
    "paper",
    "scissors"
]

user_score = 0
cpu_score = 0

print("Welcome to Rock, Paper, Scissors! \nAmerica's 17.5th Favorite Pastime (according to me)!")
print('Let us begin! \nChoose one of three options. \n1. Rock \n2. Paper \n3. Scissors')
print('If you wish to quit, write "quit"')

while True:
    user_choice = input('What is your choice? ').lower()

    cpu_choice_num = random.randint(0,2)
    cpu_choice = options[cpu_choice_num]

    if user_choice == "quit":
            print("Thanks for playing!")
            break

    if user_choice not in options:
        print("Oops! Invalid Option. Please Try Again... ")
        continue

    print(f"You played {user_choice}. \nCPU played {cpu_choice}")

    if user_choice == cpu_choice:
        print("TIE!")
    else:
        match user_choice:

            case "rock":
                if cpu_choice == "scissors":
                    print("VICTORY!")
                    user_score += 1
                else:
                    print("DEFEAT!")
                    cpu_score += 1

            case "paper":
                if cpu_choice == "rock":
                    print("VICTORY!")
                    user_score += 1
                else:
                    print("DEFEAT!")
                    cpu_score += 1

            case "scissors":
                if cpu_choice == "paper":
                    print("VICTORY!")
                    user_score += 1
                else:
                    print("DEFEAT!")
                    cpu_score += 1
    
    print(f'{user_score}-{cpu_score}')

        

        