input_1 = 0
input_2 = 0

intro_text = '''"+" for addition.
"-" for subtraction.
"*" for multiplacation.
"/" for division.
"%" for modulo.
"^" for exponentiation.
"//" for rounded division.'''

valid_inputs = [
    "+",
    "-",
    "*",
    "/",
    "%",
    "^",
    "//"
]

print("Welcome to the Calculator")

while True:
    print(intro_text)
    operator = input("Choose an operator: ")

    if operator == "leave":
        exit()

    if operator not in valid_inputs:
        print("Oops! Invalid Input! Try Again.")
        continue
    
    input_1 = float(input("What is your first operand? "))
    input_2 = float(input("How about your second operand? "))

    match operator:
        case "+":
            print(f"{input_1} added to {input_2} is equal to {input_1 + input_2}")
        case "-":
            print(f"{input_1} subtracted by {input_2} is equal to {input_1 - input_2}")
        case "*":
            print(f"{input_1} multiplied by {input_2} is equal to {input_1 * input_2}")
        case "/":
            print(f"{input_1} divided by {input_2} is equal to {input_1 / input_2}")
        case "%":
            print(f"The remainder of {input_1} divided by {input_2} is {input_1 % input_2}")
        case "^":
            print(f"{input_1} to the power of {input_2} is equal to {input_1 ** input_2}")
        case "//":
            print(f"The quotient of {input_1} and {input_2} rounded down is {input_1 // input_2}")

    continue_confirmation = input('Do you wish to continue? If not, type "leave" and if so type anything: ')

    if continue_confirmation == "leave":
        exit()