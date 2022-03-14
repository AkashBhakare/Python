# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:40:53 2021

@author: Akash
"""

def printAscending(limit):
    print(f"Integers in the range of 1..{limit} are:")
    for counter in range (1,limit+1):
        print(counter)
        
  
def printDescending1(start):
    print(f"Integers in the range of {start}..1 are:")
    while start >= 1:
        print(start)
        start = start - 1
        
    
def printDescending2(limit):
    for counter in range (limit,0,-1):
        print(counter)