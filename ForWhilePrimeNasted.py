# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:54:46 2021

@author: Akash
"""

# Print all prime numbers in the range of 1 to n

import math

print("Program to check if the given number is Prime:")
message = "Enter the the number to check if it's Prime or Enter 0 to stop : "
number = int(input(message))

while(number != 0):
    isFactorFound = False
    #inner for loop
    for counter in range(2, (int(math.sqrt(number))+1)):
        if(number % counter == 0):
            isFactorFound = True
            break
    # end of for loop
    
    if(isFactorFound == True):
        print("The number ",number," is not prime",sep="")
    else:
        print("The number ",number," is prime",sep="")
        
    number = int(input("Please enter the next number to check or '0' to stop: "))
    
    
