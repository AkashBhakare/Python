# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:39:35 2021

@author: Akash
"""


limit = 5
sqr_list = []
for num in range(1,limit+1):
    sqr_list.append(num**2)
    
print(sqr_list)

# Generator Expression

limit = 5

# List Comprehension
nums_squared_lc = [num**2 for num in range(1,limit+1)]

print(nums_squared_lc)

print("the Squares are as follows :")
for sqr in nums_squared_lc:
    print(sqr)

# Generator Expression
nums_squared_gc = (num**2 for num in range(1,limit+1))
print(nums_squared_gc)

for counter in range(1,limit+1):
    print(next(nums_squared_gc))


oddNumberGenerator = (((x*2)-1) for x in range(1,1001))

print(next(oddNumberGenerator))
print(next(oddNumberGenerator))
print(next(oddNumberGenerator))
oddNumberGenerator.close()
print(next(oddNumberGenerator))


# Generators are great way to Optimize Memory usage
import sys

# sys.getsizeof()
# Return the size of an object in bytes. 
# The object can be any type of object.

nums_squared_lc = [i * 2 for i in range(1,100001)]
print("Memory used by list Comprehension",
      sys.getsizeof(nums_squared_lc)," bytes")

nums_squared_gc = (i ** 2 for i in range(1000001) )
print("Memory used by Generator Expression",
      sys.getsizeof(nums_squared_gc), " bytes")

print(next(nums_squared_gc))