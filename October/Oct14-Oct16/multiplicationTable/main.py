number = int(input("What number do you want the multiples of? "))
iteration = 0

print(f"The multiples of {number} from 0-12 are: ")
for iteration in range (0, 13):
    print(f"{number} * {iteration} = {number * iteration}")
    print("-----")
