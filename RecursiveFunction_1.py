# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:31:18 2021

@author: Akash
"""

def printAscending(limit):
    for counter in range (1,limit+1):
        print(counter)
    
    
def printAscendingRec(number):
    if number != 1:
        printAscendingRec(number-1)
    print(number)
    
    
    
#def printDescendingNonRec(start):
#    while start >= 1:
#        print(start)
#        start = start - 1
    
def printDescending(limit):
    for counter in range (limit,0,-1):
        print(counter)
    

# print numbers in descending order (1..n)
def printDescendingRec(number):
    print(number)
    if number != 1:
        printDescendingRec(number - 1)
    return

if __name__ == '__main__':
    num = int(input("Enter a number:"))
    print('Numbers in Ascending order:')
    printAscending(num)
    print('Numbers in Descending order:')
    printDescending(num)