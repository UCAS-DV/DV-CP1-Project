import math

def squareArea(length):
    return length ** 2

def rectangleArea(length, width):
    return length * width

def triangleArea(height,base):
    return 0.5 * base * height

def circleArea(radius):
    return math.pi * (radius**2)

def trapezoidArea(top,bottom,height):
    return (top + bottom) * height * 0.5


while True:
    intro = '''What shape do you want to calculate the area of?
Square - Type "1"
Rectangle - Type "2"
Triangle - Type "3"
Circle - Type "4"
Trapezoid - Type "5"
If you want to leave, type "_stop"'''

    print(intro)
    answer = -1
    shape = input("What's your selection? ")

    if shape == "_stop":
        exit()

    units = input("What's the abbreviation of the units you want to measure in? ") + "^2"

    match shape:
        case "1":
            answer = squareArea(float(input("What is the side length of your square? ")))
            print(f"The area of your square is {answer}{units}")
        case "2":
            answer = rectangleArea(float(input("What's the length of your rectangle? ")), float(input("What's the height of your rectangle? ")))
            print(f"The area of your rectangle is {answer}{units}")
        case "3":
            answer = triangleArea(float(input("What's the base length of your triangle? ")), float(input("What's the height of your triangle? ")))
            print(f"The area of your triangle is {answer}{units}")
        case "4":
            answer = circleArea(float(input("What's the radius of your circle? ")))
            print(f"The area of your circle is ~{answer}{units}")
        case "5":
            answer = trapezoidArea(float(input("What's the length of the top side of your trapezoid? ")), float(input("What's the length of the bottom side of your trapezoid? ")), float(input("What's the height of your trapezoid? ")))
            print(f"The area of your trapezoid is {answer}{units}")
        case _:
            print("Sorry! Invalid Input. Please input a valid input! ")

        

    