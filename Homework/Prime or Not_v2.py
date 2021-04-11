"""
Christopher Pile
Student ID 2526666
Date last modified 1/03/2021
"""

while True:
    number = input("Please enter a whole number greater than 1: ")
    if number.isnumeric():
        number = int(number)
        break
    else:
        print("*ERROR: PLEASE ENTER A WHOLE NUMBER GREATER THAN 1*")

# determining if 'i' is prime by checking for potential divisors less than that number

for i in range(2, number):
    if number % i == 0:
        print(number, " is not a prime number because ", i, " * ", number//i, " = ", (number//i) * i)
        print("The smallest divisor (besides 1) of ", number, " is ", i)
        break
else:
    print(number, " is a prime number")
