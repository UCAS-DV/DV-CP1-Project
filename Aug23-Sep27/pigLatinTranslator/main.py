vowels = [
    "a",
    "e",
    "i",
    "o",
    "u"
]

def Translate(word=""):
    translated_word = ""
    vowel_location = 1
    for letter in word:
        if letter in vowels:
            vowel_location = word[word.find(letter)]
    print(vowel_location)
    translated_word = word[vowel_location:] + word[:vowel_location] + "ay"

    return translated_word

while True:
    user_input = input("What word do you want to translate into Pig Latin? ")
    if user_input == "_stop":
        exit()
    print(f'"{user_input}" in Pig Latin is "{Translate(user_input)}"')