# Darius Vaiaoga, "RAID: Fibonacci Sequence Generator", Period 2

amount_of_numbers = 0
index = 0
num_one = 0
num_two = 1
fibonacci_num = 1

while True:
    user_input = input("How many Fibonacci numbers do you want to be generated? ")

    if user_input == "underscore stop":
        exit()
    else:
        amount_of_numbers = int(user_input) - 2

    print(num_one)
    print(num_two)
    while index < amount_of_numbers:    
        fibonacci_num = num_one + num_two
        print(fibonacci_num)
        num_one = num_two
        num_two = fibonacci_num
        index += 1
    num_one = 0
    num_two = 1
    index = 0