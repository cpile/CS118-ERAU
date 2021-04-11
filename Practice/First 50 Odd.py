"""
Christopher Pile
Student ID: 2526666
Date last modified: 04/03/2021
"""
file_name='odds.txt'
fh = open(file_name, 'w')
for i in range(1, 100, 2):
    if i == 99:
        fh.write(f"{i}")
    else:
        fh.write(f"{i},")
fh.close()

fh = open(file_name, 'r')
s = fh.read()
lst = s.split(',')
print(len(lst))
print(lst[16])