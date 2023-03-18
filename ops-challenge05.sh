#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 16 Mar 2023
# Purpose: Clearing logs
# Reference: https://www.networkworld.com/article/3538471/how-to-compress-files-on-linux-5-ways.html
# https://www.baeldung.com/linux/clear-file-contents

# Main

# Print to the screen the file size of the log files before compression 
# /var/log/syslog
# /var/log/wtmp
wc -c /var/log/syslog | awk '{print $1}'
wc -c /var/log/wtmp | awk '{print $1}'

# Compress the contents of the log files listed below to a backup directory     zip ./bigfile.zip bigfile
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
makdir ./BackupTest
today=$(date +"%Y-%m-%d")
pwd
zip ./BackupTest/syslog-${today}.zip /var/log/syslog
zip ./BackupTest/wtmp-${today}.zip /var/log/wtmp


# Clear the contents of the log file
cp /dev/null /var/log/syslog
cp /dev/null /var/log/wtmp

# Print to screen the file size of the compressed file
wc -c ./BackupTest/syslog-${today}.zip | awk '{print $1}'
wc -c ./BackupTest/wtmp-${today}.zip | awk '{print $1}'

# Compare the size of the compressed files to the size of the original log files
echo "Size of syslog before cempressing"





#END