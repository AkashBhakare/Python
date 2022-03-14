# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:50:09 2021

@author: Akash
"""
# Print all prime numbers in the range of 1 to n

import math

limit = int(input("Please enter a integer : "))
print("Prime numbers in the range of 1 to",limit,"are as follows:")

#outer for Loop
for number in range(1,(limit+1)):

    isFactorFound = False
    #inner for loop
    for counter in range(2, (int(math.sqrt(number))+1)):
        if(number % counter == 0):
            isFactorFound = True
            break
    # end of for loop
    
    if(isFactorFound == False):
        print(number)
    
    
