questions = [
    "What was the first video game console?",
    "What year did the video game market completely crash?",
    "What video game is commonly accredited for saving the video game industry?",
    "What was the first major 3D video game console?",
    "What were the major video game console brands in the 90s?"
]

easy_questions = [
    "What does NES stand for?",
    "Which country is Nintendo based in?",
    "Which of these companies owns the Xbox brand?",
    "What was the best selling game on the NES?",
    ""
]

ques_one_ans = [
    "A. Magnavox Odyssey",
    "B. Nintendo Entertainment System",
    "C. Atari 2600",
    "D. Game & Watch"
]

quesion_ans = [
    "A. 1989",
    "B. 1993",
    "C. 2010",
    "D. 1983",
    "A. Sonic the Hedgehog",
    "B. Donkey Kong",
    "C. Super Mario Bros.",
    "D. The Legend of Zelda",
    "A. Playstation",
    "B. Sega Saturn",
    "C. Nintendo 64",
    "D. Sega Dreamcast",
    "A. Sega, Nintendo, Playstation",
    "B. Atari, Nintendo, Playstation",
    "C. Xbox, Nintendo, Playstation",
    "D. Sega, Nintendo, Xbox"
]

user_answers = []

question = 0
score = 100
correct = True

def report_answer(user_answer="", correct_answer=""):
    user_answers.append(f"{questions[question]} \nYour Answer: {user_answer.upper()} \nCorrect Answer: {correct_answer.upper()}")

print("~-~-~-~-~-Video Game History Quiz~-~-~-~-~-")

while question < 5:
    if correct:
        print(questions[question])
    else:
        print(easy_questions[question])
    answer = input("What is your answer? (input letter) \n").lower

    if answer not in ["a", "b", "c", "d"]:
        print("Oops! Invalid Answer. Please Try Again.")
        continue

    



