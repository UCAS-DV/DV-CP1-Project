# Darius Vaiaoga, "SkillPractice: Average Grade", Period 2


num_of_classes = int(input("How many classes do you have? "))

grades = [0]

grades_entered = False
class_num = 1

total_grade_value = 0
grade_average = 0

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
    
    grades.append(int(input(f"What is your grade (in %) in your {ordinal} class? ")))
    class_num += 1

for grade in grades:
    total_grade_value += grade
    grade_average = total_grade_value / num_of_classes

    

print(f"Alright! Your average grade throughout all of your classes is {grade_average}%")






            