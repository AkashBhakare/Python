# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:11:09 2021

@author: Akash
"""

total_rows = int(input("Howy many rows do you want to print ?"))
for row in range(1,(total_rows+1)):
    #print space
    for col in range(0, (total_rows-row)):
        print(" ",end = "")
        
        #print star
    for col in range(1,(row+1)):
        print("*",end=" ")
    print()