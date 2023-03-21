#!/usr/bin/env python3

# Script: Ops 301 Class 06 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 20 Mar 2023
# Purpose: Usage of OS module
# -------------------------------
# The Python module “os” must be utilized
# At least three variables must be declared in Python that contain results of bash operations
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:
# whoami
# ip a
# lshw -short
# -------------------------------


# Main
##########################################
import os

whoAmI = os.popen("whoami")
whoAmI = whoAmI.read()

ip_a = os.popen("ip a")
ip_a = ip_a.read()

lshw_short = os.popen("sudo lshw -short")
lshw_short = lshw_short.read()

line = "-----------------------------"


print(line, "whoami", line)
print(whoAmI)
print(line, "ip a", line)
print(ip_a)
print(line, "lshw -short", line)
print(lshw_short)


##########################################
#END