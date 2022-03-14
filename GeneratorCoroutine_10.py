# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:41:35 2021

@author: Akash
"""


def multiplyIt(param1, param2):
    result = param1 * param2
    return result

def sportsGenerator():
    counter = 1
    print("getting sport : ",counter)
    counter = counter + 1
    yield("Cricket")
    print("getting sport : ",counter)
    counter = counter + 1
    yield("FootBall")
    print("getting sport : ",counter)
    counter = counter + 1
    yield("Hockey")
    print("getting sport : ",counter)

    
## returns a  iterator, i.e. a generator object
sport = sportsGenerator() 
## The iterator can be used by calling the next method.
sportName = next(sport)
print("Sport : ", sportName)
sportName = next(sport)
print("Sport : ", sportName)
sportName = next(sport)
print("Sport : ", sportName)



val = multiplyIt(10,2)
print(val)
print(val)
val = multiplyIt(3,4)
print(val)
val = multiplyIt(5,6)