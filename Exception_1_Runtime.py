# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:32:57 2021

@author: Akash
"""

# Runtime Exception : Maximum recursion limit exceeded
# It is possible to change the recursion depth 
# limit by using
# sys.setrecursionlimit(limit)
# You can check what the current parameters of the 
# limit are by running:
# sys.getrecursionlimit()

#Gracefully exit

import time
import sys

def countdown(n:int):
    if n <= 0:
        print ("Blastoff!")
    else:
        print( n )
        # time.sleep(1)
        countdown(n-1)
        
def countup(depth):
    print(depth)
    # time.sleep(1)
    countup(depth+1)


def cursing(depth):
    try:
        print(depth)
        cursing(depth + 1) # actually, re-cursing
    except RecursionError as re:
        print(f'I recursed {depth-1} times!')
        # print(re.__str__)
       
        
  
if __name__ == '__main__':
    # countdown(10)
  # 
    sys.setrecursionlimit(50)
##    countdown(-1)
##    countup(1)
##    cursing(0)  
    
    try:
##        countup(1)
        countdown(400)
    except RecursionError as err:
        print("Error Message :",err)
    else:
        print("Thank You!")
    finally:
        print("Finally!")
