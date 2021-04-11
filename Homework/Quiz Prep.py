"""
Christopher Pile
Student ID: 2526666
Date last modified: 22/02/2021
"""

# 4.13(d)

s = 'abcdefghijklmnopqrstuvwxyz'

# slice of 's' excluding first and last characters

sl = s[1:25]
print(sl)

# 4.15(c)

s = '10&20&30&40&50&60'

s = s.split("&")
print(s)
print('')

# 4.18

s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was...  '''
print(s)
print('\n')

# a
"""
chrs = [",", ".", ";", "\n"]
for c in chrs:
    newS = s.replace(c, '')
"""
newS = ""
for i in s:
    if i == ".":
        newS = newS + ""
    elif i == ",":
        newS = newS + ""
    elif i == ";":
        newS = newS + ""
    elif i == "\n":
        newS = newS + ""
    else:
        newS = newS + i

print(newS)

# b

newS = newS.strip()
print(newS)

# c

newS = newS.lower()
print(newS)

# d

count = newS.count('it was')
print(count)

# e

newS = newS.replace('was', 'is')
print(newS)

# f

listS = newS.split(" ")
print(listS)


