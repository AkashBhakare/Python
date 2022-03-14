# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:30:49 2021

@author: Akash
"""

## Display Factorial of a given number

number = int(input("Please enter an integer"))
counter = 1
factorial = 1
while counter <= number:
    factorial = factorial * counter
    counter = counter + 1

print("Factorial of ",number,"is",factorial)
