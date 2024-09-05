# Darius Vaiaoga, "SkillPractice: Setting, Resetting, and Resetting", Period 2

# Define Variables
faculty = 32
students = 100
guests = students * 2

# Reset Variables
students -= 1
faculty -= 3
faculty += 1
guests = students * 2
guests -= 15

# Calculate Number of Tables needed then round it up
tables = (students + faculty + guests) / 12
print(tables)