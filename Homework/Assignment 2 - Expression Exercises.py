"""
Christopher Pile
Student ID: 2526666
Last modified: 09/02/2021
"""

"""Exercise 2.11(b)"""

kids = [[9, 17], [10, 24], [11, 21], [12, 27]]
avgAge = (kids[0][0]*kids[0][1] + kids[1][0]*kids[1][1] + kids[2][0]*kids[2][1] + kids[3][0]*kids[3][1]) / 89
print("The average age of the group of kids is: " + str(round(avgAge)))

"""Exercise 2.11(d)"""

print("\n61 can go into 4356: " + str(4356/61) + " times.")

"""Exercise 2.14(b & d)"""

s = "goodbye"

print("\nIs g the 7th character of 'goodbye': ", end="")
print("g" == s[6])

print("Is the penultimate character 'x': ", end="")
print('x' == s[5], end="")

"""Exercise 2.16(e)"""

first = "John"
middle = "Fitzgerald"
last = "Kennedy"

fullname = first + " " + middle + " " + last
print("\n")
print(fullname)
