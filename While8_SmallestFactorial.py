# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:38:34 2021

@author: Akash
"""

## Smallest Factor other than 1, of a given number

num = int(input("Enter a integer : "))

counter = 2

while counter <= num:
    ## check if the number is completely divisible by counter
    if num % counter == 0 : 
        print("The smallest factor of",num,"is",counter)
        break  ## terminates the loop when factor is found
    
    counter = counter + 1
## end of the loop
