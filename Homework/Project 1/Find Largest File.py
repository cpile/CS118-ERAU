"""
Author: Christopher Pile
Student ID: 2526666
Date last modified: 05/04/2021
"""

import os

# dirs = [C:\Users\pilecd\Desktop\Largest File]

baseDir = input("Please enter the start directory: ")  # getting directory name from user

if os.path.isdir(baseDir):  # checking to see if given directory does exist
    for dirpath, dirnames, dirfiles in os.walk(baseDir):
        files = [os.path.join(dirpath, i) for i in dirfiles]

# for i in range(min(10, len(files))): # printing largest 10 files or largest files if len(files) < 10








