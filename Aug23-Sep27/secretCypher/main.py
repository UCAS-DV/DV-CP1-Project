def shiftLetter(character, shift):
    if character != " ":
        character_value = ord(character)
        if (character_value + shift) > 90:
            character = 65
            shift = (character_value + shift) - 91
            return(chr(character + shift))
        return chr(character_value + shift)
    else:
        return character   

def EncodeMessage(message="", inputed_shift=0):
    encoded_message = ""
    for char in message.upper():
        encoded_message += shiftLetter(char, inputed_shift)
    return encoded_message

while True:
    user_shift = -1
    user_message = input("What message would you like to encode? ")
    while user_shift < 0 or user_shift > 25:
        user_shift = int(input("How far do you want to shift the message? (shift cannot be less than 0 or more than 25) "))

    print(f"You chose to encode {user_message} with a shift of {user_shift}.")
    print(f"You're encoded message is: {EncodeMessage(user_message, user_shift)}")

    if input('Do you want to encode more messages? If so, type anything, if not, type "_exit" ') == "_exit":
        exit()
        

