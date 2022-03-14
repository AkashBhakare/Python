# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:18:10 2021

@author: Akash
"""

def addition(x, y):
    return x + y

ans = addition(2,3)
print(ans)

ans = addition("Hi"," Bye")
print(ans)

def add(x:int, y:int)->int:
    return x+y

import math

def circuference(radius: float) -> float:
    '''
    parameters
    ----------
    radius : float
       Radius of the Circle in cm.
       
    return
    -------
    float
        Reruns Circuference in sqcm
    '''
    return 2 * math.pi * radius
     
if __name__ == '__main__':
    ans = addition(2,3)
    print(ans)
    
    ans = addition("Hi","Bye")
    print(ans)
     
    ans = addition(4+5j,6+7J)
    print(ans)
    
    ans = add(2,3)
    print(ans)
    ans = add("Anil","3")
    print(ans)
    print("Information of function add:\n\t")
    print(add.__annotations__)
    print(circuference(4.5))
    #print(circuference("abcd"))
    print("Information of function circumference:\n\t")
    print(circuference.__annotations__)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     