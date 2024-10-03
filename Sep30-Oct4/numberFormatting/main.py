number = float(input("What number would you like to be formatted? "))

strings = [
    "Your number seperated into thousands is {:,}",
    "Your number as a decimal number is {:.4f}",
    "Your number as a percentage is {:.2%}",
    "Your number in dollars is ${:.2f}"
] 

for line in strings:
    print(line.format(number))