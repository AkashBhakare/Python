# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:37:47 2021

@author: Akash
"""

# iterator with Sentinal

print("using range function")
for counter in range(1,6):
    print(counter)
    

print("using range object")
myRange = range(1,6)
for counter in myRange:    
    print(counter)
    
sentinal = 7
# Error : Since range() is iterable and not callable
myIterator = iter(range(1,10),sentinal)

while(True):
    print(next(myIterator))
    
