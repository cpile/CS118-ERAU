def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def mod(a, b):
    return a % b


d = {'+': sum, '-': sub, '*': mul, '%': mod}

print(type)


op = input("Please enter an operation (separated by spaces, e.g. '1 + 17'): ")

lst = op.split()

a = int(lst[0])
b = int(lst[2])
f = d[lst[1]]
print(f(a,b))

"""
if lst[1] == '+':
    print(sum(int(lst[0]), int(lst[2])))
elif lst[1] == "-":
    print(sub(int(lst[0]), int(lst[2])))
else:
    print(mul(int(lst[0]), int(lst[2])))
"""


