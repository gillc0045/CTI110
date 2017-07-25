# Write a program that asks for the length and width of rectangle's.
# The program should tell the user which rectangle has the greater area,
# or if the areas are the same.

# Enter the Length of Rectangle_1
length_1 = int(input('Enter the length of Rectangle_1: '))
#
# Enter the Width of Rectangle_1
width_1 = int(input('Enter the width of Rectangle_1: '))
#
# Area  of Rectangle_1 = length_1 * width_1
areaOfRectangle_1 = length_1 * width_1

# Enter the Length of Rectangle_2
length_2 = int(input('Enter the length of Rectangle_2: '))
#
# Enter the Width of Rectangle_2
width_2 = int(input('Enter the width of Rectangle_2: '))
#
# Area  of Rectangle_2 = Length * Width
areaOfRectangle_2 = length_2* width_2


# Print the results
print('The area of Rectangle_1 is ',areaOfRectangle_1)
print('The area of Rectangle_2 is ',areaOfRectangle_2)

# Compare the area of Rectangle_1 to the area of Rectangle_2
if areaOfRectangle_1 > areaOfRectangle_2:
    print('The area of Rectangle_1 is larger than the area of Rectangle_2')
elif areaOfRectangle_1 < areaOfRectangle_2:
    print('The area of Rectangle_2 is larger than the area of Rectangle_1')
else:
    print('The area of Rectangle_1 is equal to the area of Rectangle_2')
