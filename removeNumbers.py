"""
Author: James Musacchio
Version: 1
Description:
Simple script to remove the leading numbers + an underscore from files in a specified directory.
For example: you'd begin with 1234_example.pdf, 567_test.exe. After running this script with an argument passing
the directory where these files are located,you would end up with example.pdf and test.exe.
"""

import os, sys, re

INPUTDIR = sys.argv[1]

FILE_LIST = []
for root, dirs, files in os.walk(INPUTDIR):
    for file in files:
        fullPath = os.path.join(INPUTDIR, file)
        FILE_LIST.append(fullPath)

for file_name in FILE_LIST:
    y = re.search("[0-9]*_", file_name)
    if  y is not  None:
        x = re.sub("[0-9]*_", "", file_name)
        os.rename(file_name, x)
        print(x)
