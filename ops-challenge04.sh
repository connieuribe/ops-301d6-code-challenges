#!/bin/bash

# Script: Ops 301 Class 04 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 16 Mar 2023
# Purpose: Conditionals in Menu Systems

# Main

# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit

menu (){
    echo "---- MENU OPTIONS --- 
    [1] Print Hello World 
    [2] Ping Self 
    [3] IP Info 
    [4] EXIT "
}

# The program should next use a conditional statement to evaluate the user’s input, 
# then act according to what the user selected.
# Use a loop to bring up the menu again after the request has been executed.

while [[ true ]]
do
    menu
    # Next, the user input should be requested.
    read -p "ENTER OPTION: " ans_input 

    if [[ $ans_input -eq 1 ]]
    then
        echo
        echo "Hello World"
        echo
    elif [[ $ans_input -eq 2 ]]
    then
        echo
        ping -c1 127.0.0.1
        echo
    elif [[ $ans_input -eq 3 ]]
    then
        echo
        ip a
        echo
    elif [[ $ans_input -eq 4 ]]
    then
        echo
        echo "Exiting . . ."
        break
    else
        break
    fi

done

echo BYE
#END