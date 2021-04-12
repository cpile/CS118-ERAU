"""
Author: Christopher Pile
Student ID: 2526666
Date last modified: 11/04/2021
"""


def add(x, y):  # adds two numbers together
    return x + y


def mult(x, y):  # finds the product of two numbers
    return x * y


def divide(x, y):  # divides two numbers
    return x / y


def sub(x, y):  # finds the difference between two numbers
    return x - y

# puts math formulas in a dictionary so they can be called upon by using the operator as the key


formulas = {'+': add, '-': sub, '/': divide, '*': mult}


def math(operand, numbers):  # takes in the user input operator and numbers and calls the right formula
    return formulas[operand](int(numbers[0]), int(numbers[1]))


def main():  # asks user for a mathematical operator and two numbers and returns desired operation
    while True:
        operand = input("Please enter a mathematical operator (+, *, /, -): ")
        if operand in ('+', '-', '*', '/'):
            nums = input("Please enter two numbers separated by a space: ")
            lst_nums = nums.split(' ')
            print(f" {lst_nums[0]} {operand} {lst_nums[1]} = {math(operand, lst_nums)}")
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
