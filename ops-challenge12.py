#!/usr/bin/env python3
import requests
from requests.exceptions import HTTPError

# Script: Ops 301 Class 12 Ops Challenge Solution
# Author: Connie Uribe Chavez
# Date of lates revision: 28 Mar 2023
# Purpose: HTTP Request
# Reference: https://realpython.com/lessons/responses-status-codes/
# -------------------------------



# Prompt the user to type a string input as the variable for your destination URL.
# Prompt the user to select a HTTP Method


url = input ( "Enter a URL: ")
for request in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']:
    print(request)
http_type = input( "Enter the request: ")
user_request = http_type + "(" + url + ")"
print("Your request: ", user_request)
yn = input("Enter Y to proceed or N to terminate the request:   " )


# Print to the screen the entire request your script is about to send. Ask the user to 
#confirm before proceeding.

if (yn == "Y"):
    #The following code is from https://realpython.com/lessons/responses-status-codes/
    try:
        print("4")
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    else:
        print('Success!')
else:
    print("Closing program . . .")



# For the given header, translate the codes into plain terms that print to the screen; 
#for example, a 404 error should print Site not found to the terminal instead of 404.
#For the given URL, print response header information to the screen.