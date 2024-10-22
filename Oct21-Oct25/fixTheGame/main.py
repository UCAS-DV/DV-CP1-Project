import random

def start_game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False

    while not game_over:

        # The code was saving the guess as a strong rather than an integer.
        # So when the code stopped when it saw that it was trying to compare a string
        # and an integer. This was a runtime error.
        # Original Code:
        # guess = input("Enter your guess: ")
        guess = int(input("Enter your guess: "))

        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True    
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  

        # This was a logic error where the game wouldn't end if you surpassed the
        # maximum number of attempts because the game code didn't increment the number
        # of attempts every guess.
        attempts += 1
        continue

    print("Game Over. Thanks for playing!")

start_game()