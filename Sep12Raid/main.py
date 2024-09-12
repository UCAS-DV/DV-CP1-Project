# Returns the product of two inputs, x and y
def calculate_area(width, height):
    area = width * height
    return area

# Multiplies the product of a and b by c and then returns that new product.
def calculate_volume(threeD_width, threeD_height, threeD_length):   
    area_of_side = calculate_area(threeD_width, threeD_height)
    volume = area_of_side * threeD_length
    return volume

# Calculates the size of "flat_thing" by multiplying thing1 and thing2 together
square_width = 5
square_height = 3
square_area = calculate_area(square_width, square_height)
# Outputs the size of flat_thing
print(f"The square's area is: {square_area}")

# Calculates the size of "big_thing" by multiplying foo, bar, and baz together 
cuboid_width = 4
cuboid_height = 6
cuboid_length = 2
cuboid_volume = calculate_volume(cuboid_width, cuboid_height, cuboid_length)
# Outputs the size of big thing
print(f"The cuboid's volume is: {cuboid_volume}")