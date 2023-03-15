#!/bin/bash

# Script: Ops 301 Class 02 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 14 Mar 2023
# Purpose: Appends the current date and time to the filename

# Main

#Copies /var/log/syslog to the current working directory
#Appends the current date and time to the filename
today=$(date +"%Y-%m-%d")
cp /var/log/syslog syslog-${today}


# End