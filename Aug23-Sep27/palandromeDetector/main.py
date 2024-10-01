# Darius Vaiaoga, "SkillPractice: Palandrom", Period 2

word = ""
word_length = 0

while True:
    word = input("What word do you want to check? ")
    word_length = len(word) - 1
    reversed_word = ""
    index = 0

    if word == "underscore stop":
        exit()

    for character in word:
        reversed_word += word[word_length - index]
        index += 1

    if reversed_word.lower() == word.lower():   
        print(f"{word} is a palindrome!") 
    else:
        print(f"{word} isn't a palindrome. Reversing it gives you {reversed_word}")