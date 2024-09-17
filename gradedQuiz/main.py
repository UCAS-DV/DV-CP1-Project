# Darius Vaiaoga, "ProficiencyTest: Graded Quiz", Period 2

set_up_instructions = '''Hello, welcome to Darius' Stupidly Hard, Near Impossible, Truly Devastating, Completely Perplexing Math Quiz of 
Mathematics!
This quiz is certainly a doozy so it's highly recommended you take some time to mentally prepare yourself.
When you are ready, type anything and then press "Enter"'''

score = 100

print("========== Set Up ==========")
input(set_up_instructions + " ")

while True:   

    print("========== Math Quiz ==========")

    if float(input("1/5. What is 1 + 3? ")) != 4:
        score -= 20
    if float(input("2/5. What is 4-2? ")) != 2:
        score -= 20
    if float(input("3/5. What is 10 / 5?" )) != 2:
        score -= 20
    if float(input("4/5. What is 3 x 5? ")) != 15:
        score -= 20
    if float(input("5/5. What is 3 - 0? ")) != 3:
        score -= 20

    print(f"Congratualations! You survived! Your final score is {score}%")
    input('If you want to retake the quiz, type anything and then press "Enter"')



