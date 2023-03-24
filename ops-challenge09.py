#!/usr/bin/env python3
# Script: Ops 301 Class 09 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 23 Mar 2023
# Purpose: Working with If...then statement
# -------------------------------
# if statements using these logical conditionals below. 
# Each statement should print information to the screen depending on if the condition is met.


# Create an if statement using a logical conditional of your choice and include 
# elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif 
# are not met.

a = input ("Enter a a value for a: ")
b = input ("Enter a a value for b: ")



if a != b: print(a, " is not equal to ", b)
elif a == b: print(a, " is equal to ", b)

    

if a >= b: print (a, " is greater than or equal to ", b)  # Greater than or equal to: a >= b
elif a <= b: print(b, " is greater than or equal to ", a) # Less than or equal to: a <= b


if a > b: print (a, " is greater")
elif a < b: print(b, " is greater")

