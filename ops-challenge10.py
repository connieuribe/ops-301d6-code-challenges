#!/usr/bin/env python3
import os
# Script: Ops 301 Class 09 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 23 Mar 2023
# Purpose: Using file handling commands
# -------------------------------

#main
# Using file handling commands, create a Python script that creates a new .txt file, 
# appends three lines, prints to the screen the first line, then deletes the .txt file.

#create file
temp = open("newfile.txt", "w") 
#appends 3 lines
temp.write("This is the first line \nThis is the second line \nThis is the third line \n")
temp.close()
#read the file and  gets the lines
temp = open("newfile.txt", "r")
lines = temp.readlines()
temp.close()
#iterate through lines and prints the first line
count = 0
for line in lines:
    if(count == 0):
        print(line)
        break
    count += 1


#Delete the text file
os.remove("newfile.txt")
#END