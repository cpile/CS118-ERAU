"""
Christopher Pile
Student ID: 2526666
Date last modified: 27/02/2021
"""


fh = open('treasure.txt')
s = fh.read()
fh.close()

chrs = "'.,!:;?\n\""
for c in chrs:
    s = s.replace(c, ' ')

words = s.split()
print(words)

print("silver is in the book ", words.count("silver"), " times.")
print("Silver is in the book ", words.count("Silver"), " times.")
