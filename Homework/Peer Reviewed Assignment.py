"""
Christopher Pile
Student ID: 2526666
Date Last Modified: 02/16/2021
"""

# Exercise 3.18

a = 3
b = 4
c = 5

if a < b:
    print("a < b?", end=': ')
    print('OK')

if c < b:
    print("c < b?", end=': ')
    print('OK')

if a + b == c:
    print("a + b = c?", end=': ')
    print('OK')

if pow(a, 2) + pow(b, 2) == pow(c, 2):
    print("a^2 + b^2 = c^2?", end=': ')
    print('OK')

print('')

# Exercise 3.22

lst = list(range(0, 45))

for i in lst:
    if pow(i, 2) % 8 == 0:
        print(i)

print('')

# Exercise 3.23

# 0 1

for i in range(2):
    print(i, end=' ')
print('')

# 0

for i in range(1):
    print(i)
# 3 4 5 6

for i in range(3, 7):
    print(i, end=' ')
print('')

# 1

for i in range(1, 2):
    print(i)

# 0 3

for i in range(0, 4, 3):
    print(i, end=' ')
print('')

# 5 9 13 17 21

for i in range(5, 25, 4):
    print(i, end=' ')




