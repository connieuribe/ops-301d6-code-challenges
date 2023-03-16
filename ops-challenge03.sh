#!/bin/bash

# Script: Ops 301 Class 03 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 15 Mar 2023
# Purpose: Use chmod to modify the permissions of the files in a directory

# Main


# Prompts user for input directory path. 
read -p "Enter a directory path: " dir_input

# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
read -p "Enter permission number: " num_input

# Navigates to the directory input by the user and changes all files inside it to the input setting.
cd ${dir_input}
for FILE in *; do chmod ${num_input} ${FILE}; done

# Prints to the screen the directory contents and 
# the new permissions settings of everything in the directory.
ls -l





# End