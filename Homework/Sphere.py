# Christopher Pile
# Student ID: 2526666
# January 2, 2021

import math

radius = input("Enter radius of sphere: ")
radius = float(radius)

diameter = str(radius * 2)
circumference = str((2 * math.pi) * radius)
sfc = str((4 * math.pi) * pow(radius, 2))
volume = str((4/3) * math.pi * pow(radius, 3))

print("Radius = " + str(radius))
print("Diameter = " + diameter)
print("Circumference = " + circumference)
print("Surface Area = " + sfc)
print("Volume = " + volume)


print("\nusing f-string\n")
radius = input("Enter radius of sphere: ")
radius = float(radius)

diameter = (radius * 2)
circumference = ((2 * math.pi) * radius)
sfc = ((4 * math.pi) * pow(radius, 2))
volume = ((4/3) * math.pi * pow(radius, 3))

print("Radius = " + f"{radius}")
print("Diameter = " + f"{diameter}")
print("Circumference = " + f"{circumference}")
print("Surface Area = " + f"{sfc}")
print("Volume = " + f"{volume}")

input('Press ENTER to exit')
