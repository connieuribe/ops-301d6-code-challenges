#!/usr/bin/env python3

# Script: Ops 301 Class 08 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 22 Mar 2023
# Purpose: Working with list
# -------------------------------


# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.


#Main

# Assign to a variable a list of ten string elements.
flowers = ["rose", "lily", "tulip", "jasmine", "sunflower", "dandelion", "daisy", "sweet violet", "lavender", "orchid"]

# Print the fourth element of the list.
print(flowers[3])

# Print the sixth through tenth element of the list.
print(flowers[-5:])

# Change the value of the seventh element to “onion”.
flowers[6] = "onion"
print(flowers)

#End