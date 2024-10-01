# Darius Vaiaoga, "SkillPractice: Average Grade", Period 2


num_of_classes = int(input("How many classes do you have? "))

grades = [-1,-1,-1,-1,-1,-1,-1,-1]

grades_entered = False
class_num = 1

total_grade_value = 0
grade_average = 0

if num_of_classes < 1 or num_of_classes > 8:
    while num_of_classes < 1 or num_of_classes > 8:
        num_of_classes = int(input("Oh! Sorry! You have to enter at least one class and less than 9 classes. Please try again."))



while not grades_entered:
    
    if class_num >= num_of_classes:
        grades_entered = True

    ordinal = ""
    match class_num % 10:
        case 1:
            ordinal = f"{class_num}st"
        case 2:
            ordinal = f"{class_num}nd"
        case 3:
            ordinal = f"{class_num}rd"
    if class_num % 10 >= 4:
        ordinal = f"{class_num}th"
    
    grades[class_num - 1]+= int(input(f"What is your grade (in %) in your {ordinal} class? "))
    class_num += 1

for grade in grades:
    if grade == -1:
        grade_average = total_grade_value / num_of_classes
        break

    print(grade)
    total_grade_value += grades[grade]

    

print(f"Alright! Your average grade throughout all of your classes is {grade_average}%")






            