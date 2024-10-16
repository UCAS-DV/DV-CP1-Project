print("-~-~-~-~-~ Percent-Letter Grade Converter -~-~-~-~-~")

num_of_classes = int(input("How many classes do you have? "))
iteration = 0

grades = []

while iteration < num_of_classes:
    percentage = int(input(f"What is your percent grade in class {iteration + 1}? "))

    if percentage < 60:
        grades.append(f"{iteration}. F")
    elif percentage < 64: 
        grades.append(f"{iteration}. D-")
    elif percentage < 67:
        grades.append(f"{iteration}. D")
    elif percentage < 70:
        grades.append(f"{iteration}. D+")
    elif percentage < 74:
        grades.append(f"{iteration}. C-")
    elif percentage < 77:
        grades.append(f"{iteration}. C")
    elif percentage < 80:
        grades.append(f"{iteration}. C+")
    elif percentage < 84:
        grades.append(f"{iteration}. B-")
    elif percentage < 87:
        grades.append(f"{iteration}. B")
    elif percentage < 90:
        grades.append(f"{iteration}. B+")
    elif percentage < 94:
        grades.append(f"{iteration}. A-")
    else:
        grades.append(f"{iteration}. A")

    iteration += 1

print("Your Class Grades: ")

for grade in grades:
    print(grade)