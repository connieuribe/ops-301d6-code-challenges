#!/usr/bin/env python3

# Script: Ops 301 Class 07 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 21 Mar 2023
# Purpose: Usage of variables and fuctions. 
# -------------------------------

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

# Import libraries
import os

### Read user input here into a variable
path = input ("Enter a path: ")

# Declaration of functions
def walkFunc(pArg):
    print("2")
    for (root, dirs, files) in os.walk(pArg, topdown=True):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main
walkFunc(path)

# End
