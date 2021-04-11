"""
Christopher Pile
Student ID 2526666
Date last modified 25/02/2021
"""


while True:
    number = float(input("Please enter a whole number greater than 1: "))

# checking if number is a whole number and/or greater than 1

    if number > 1:
        if not number.is_integer():
            print("*ERROR: PLEASE ENTER A WHOLE NUMBER*")
        else:
            number = int(number)
            break
    else:
        print("*ERROR: PLEASE ENTER A NUMBER GREATER THAN 1*")

# determining if 'i' is prime by checking for potential divisors less than that number

for i in range(2, number):
    if number % i == 0:
        print(number, " is not a prime number because ", i, " * ", number//i, " = ", (number//i) * i)
        print("The smallest divisor (besides 1) of ", number, " is ", i)
        break
else:
    print(number, " is a prime number")
