# Darius Vaiaoga, "ProficiencyTest: Personal Information Converter", Period 2

name = input("What is your name? ")
age = input("How old are you? ")
height = input("How tall are you (in meters)? ")
fav_number = input("And most importantly, what is your favorite integer? ")

casted_age = int(age)
casted_height = float(height)
casted_fav_number = int(fav_number)

print(f"You told me, in strings that, you're {name}; you're '{age}' years old; you're '{height}' meters tall and you're favorite number is '{fav_number}'")
print(f"After converting, I can now see that you're name is still a string which is, {name}. You're age in years is the integer, {casted_age}. You're height in meters is the floating point number, {casted_height}. And your favorite number is definitely an integer, which is {casted_fav_number}.")