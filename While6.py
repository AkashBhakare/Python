# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:31:16 2021

@author: Akash
"""

# displaying mulitplication table till 10

LIMIT = 10
number = int(input("Please enter an integer : "))
counter = 1
while counter <= LIMIT:
    print(number,"x",counter,"=",(number*counter))
    counter = counter + 1
