# Tylore
# Find more of my projects at https://github.com/TheTylore
# Version 0.1
#
#

# The purpose of this program is to select a new external drive and create selected directories in order for better file
# sorting


import os
import shutil

# vars
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

# This function selects the target drive where the newly created directories will go
def selectDrive():
    targetDrive = input("Please insert the drive letter in the format `X:`")
    if not targetDrive.isupper():
        targetDrive = targetDrive.capitalize()
    if not os.path.exists(targetDrive + '/'):
        print('Sorry, that drive does not exist. Please enter a valid destination.')
        selectDrive()
    print(targetDrive)

def makeDirs():


    print()

selectDrive()
