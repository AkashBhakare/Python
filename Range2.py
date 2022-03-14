# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:11:30 2021

@author: Akash
"""

# concatenating Range 
# itertools : Functions creating iterators for efficient looping
# from itertools import chain
import itertools

print ("Concatinated two range() function")

multiple_Of_10     = range(10, 101, 10)
first_5_integers   = range(1, 6)
concatenated_range = itertools.chain(first_5_integers, multiple_Of_10 )
print("Type is ", type(concatenated_range))

for num in concatenated_range:
    print(num, end=", ")

print ("Concatinated multiple range() function")
oddNos          = range(1,11,2)
evenNos         = range(2,11,2)
multiple_Of_5   = range(5,26,5)

concatenated_range = itertools.chain(oddNos, evenNos, multiple_Of_5)

for num in concatenated_range:
    print(num,end=", ")
    
    
# Generate a range of floating point values
for num in range(0, 5.5, 0.1):
    print (num)
    
    
    
import numpy

print("Printing float range with numpy.arange()")

for i in numpy.arange(0, 5.5, 0.5):
    print(i, end=', ')
    
for i in numpy.arange(10.5, 25.5, 2.5):
    print(i, end=', ')
    
for i in numpy.arange(-2.5, 2.6, 0.5):
    print(i, end=', ')
    
# When using a non-integer step, such as 0.1, the results will often not be consistent.
for i in numpy.arange(0.0, 1.1, 0.1):
    print(round(i,2), end=', ')
    
