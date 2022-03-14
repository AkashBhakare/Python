# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:27:53 2021

@author: Akash
"""

## sentinel-controlled loop

## Calculate the sum of all integers entered until zero is not keyed in

sum = 0

number = int(input("Enter an integer :"))
while number != 0:
    sum = sum + number
    number = int(input("Enter the next integer :"))
else:
    print("The sum is ",sum)

