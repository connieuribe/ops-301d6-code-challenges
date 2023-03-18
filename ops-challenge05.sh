#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 18 Mar 2023
# Purpose: Clearing logs
# Reference: https://www.networkworld.com/article/3538471/how-to-compress-files-on-linux-5-ways.html
# https://www.baeldung.com/linux/clear-file-contents

# Main
##########################################
# Print to the screen the file size of the log files before compression 
# /var/log/syslog
# /var/log/wtmp
wc -c /var/log/syslog | awk '{print $1}' >> syslogSize_1.txt
wc -c /var/log/wtmp | awk '{print $1}' >> wtmpSize_1.txt
echo "syslog size: "
cat syslogSize_1.txt
echo "wtmp size: "
cat wtmpSize_1.txt

# Compress the contents of the log files listed below to a backup directory     zip ./bigfile.zip bigfile
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
mkdir BackupTest
today=$(date +"%Y-%m-%d")
zip ./BackupTest/syslog-${today}.zip /var/log/syslog
zip ./BackupTest/wtmp-${today}.zip /var/log/wtmp



# Clear the contents of the log file
cp /dev/null /var/log/syslog
cp /dev/null /var/log/wtmp


# Print to screen the file size of the compressed file
wc -c $DirPath/syslog-${today}.zip | awk '{print $1}' >> syslogSize_2.txt
cat syslogSize_2.txt
wc -c $DirPath/wtmp-${today}.zip | awk '{print $1}' >> wtmpSize_2.txt
cat wtmpSize_2.txt


# Compare the size of the compressed files to the size of the original log files
echo "Size of syslog before cempressing "
cat syslogSize_1.txt
echo "Size of syslog after cempressing "
cat syslogSize_2.txt
echo ------------------------------------

echo "Size of wtmp before cempressing "
cat wtmpSize_1.txt
echo "Size of wtmp after cempressing "
cat wtmpSize_2.txt

##########################################
#END