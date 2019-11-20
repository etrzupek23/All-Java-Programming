"""
A calculator that can compute the area of a given shape as selected by the users
The calculator will be able to determine the area of the following shapes

Circle
Triangle
Pentagon

The program should do the following:
Promt the user to select a shape
Depending on the shape the user selects, calculate the area of that shape
Print the area of that shape to the user

Created by Emma T
"""

from math import pi
from math import sqrt

print "Calculator is starting up..."
print "What shape would you like to calculate the area/length for?"

option = raw_input("Enter C for circle, T for triangle, H for the hypotenuse of a right triangle, or S for the side of a right triangle: ")

if option == "C" or option == "c":
    radius = float(raw_input("Enter radius: "))
    area = pi * radius ** 2
    print "Area: %f" % area
elif option == "T" or option == "t":
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = 0.5 * base * height
    print "Area: %f" % area
elif option == "H" or option == "h":
    #formula for hypotenuse of a triangle
    sidea = float(raw_input("Enter side A (one of the legs): "))
    sideb = float(raw_input("Enter side B (the other leg): "))
    hypotenuse = sqrt(sidea * sidea + sideb * sideb)
    print "Hypotenuse: %f" % hypotenuse
elif option == "S" or option == "s":
    #formula for hypotenuse of a triangle
    sidec = float(raw_input("Enter the hypotenuse: "))
    sideb = float(raw_input("Enter the leg that you know: "))
    missingleg = sqrt(sidec * sidec - sideb * sideb)
    print "The missing leg: %f" % missingleg
else:
    print "Error! Invalid shape."

print "Exiting..."
