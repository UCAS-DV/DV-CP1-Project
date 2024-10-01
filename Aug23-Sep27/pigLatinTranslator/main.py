def Translate(word):
    translated_word = ""
    translated_word = word[1:] 
    print(translated_word)     
    translated_word += word.lower()[0] + "ay"

    return translated_word

while True:

    output = input("What word do you want to translate into Pig Latin? ")
    if output == "_stop":
        exit()
    print(f'"{output}" in Pig Latin is "{Translate(output)}"')