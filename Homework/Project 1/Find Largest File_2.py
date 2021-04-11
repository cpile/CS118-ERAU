"""
Author: Christopher Pile
Student ID: 2526666
Date last modified: 01/04/2021
"""

import os

# dirs = [C:\Users\pilecd\Desktop\Largest File]

baseDir = input("Please enter the start directory: ")  # getting directory name from user
files = []

if os.path.isdir(baseDir):  # checking to see if given directory does exist
    for dirpath, dirnames, dirfiles in os.walk(baseDir):
        for i in dirfiles:  # creating a list of all files in given directory & sub-directories
            realpath = os.path.realpath(os.path.join(dirpath, i))  # getting real path of file
            files.append((round(os.path.getsize(os.path.join(dirpath, i)) / 1024), realpath))
            # creating a list of tuples [(filesize, filename)]
    files.sort(key=lambda f: f[0], reverse=True) # sorting files by first item of tuple which is file size

for i in range(min(10, len(files))): # printing largest 10 files or largest files if len(files) < 10
    print(str(i + 1) + ".", files[i][1], ":", files[i][0], "KB")








