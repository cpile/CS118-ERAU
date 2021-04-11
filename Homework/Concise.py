"""
Christopher Pile
Student ID 2526666
Date last modified 08/03/2021
"""

import random

lst = [2]
for i in range(random.randint(4, 7)):
    while True:
        x = random.randint(2, 25)
        if lst[i] <= x < lst[i] * 2:
            lst.append(x)
            break

print(f"List: {lst} - Sum: {sum(lst)} - Median: {(lst[len(lst)//2] + lst[::-1][(len(lst)//2)]) / 2} - Avg: {'{:.2f}'.format(sum(lst) / len(lst))}")
