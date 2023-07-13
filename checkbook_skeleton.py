import json
import os

#define functions to view balance,
#make withdrawals, and make deposits

your_file = 'checkbook.json'

#check if file exists using os library
#otherwise, set balance to 0

with open (your_file, 'r') as f:
    balance = json.load(f)
    
while True:
    
    #ask for user input
    
    #do things
    
    with open (your_file, 'w') as f:
        json.dump(balance, f)