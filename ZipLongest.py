# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:03:33 2021

@author: Akash
"""

# zip() stops aggregating elements once the 
# shortest iterable passed to it is exhausted.
x = [1, 2, 3, 4, 5]  #list
y = ('a', 'b', 'c')  #tuple
result = zip(x, y)
print(list(result))


import itertools 

# zip_longest() stops aggregating elements only when the 
# longest iterable passed to it is exhausted.
result = itertools.zip_longest(x, y)
print(list(result))

# itertools.zip_longest(). 
# This function accepts any number of iterables as 
# arguments and a fillvalue keyword argument that 
# defaults to None
result = itertools.zip_longest(x, y,fillvalue='#')
print(list(result))

# Passing string to zip
str1 = "ABCDE"
str2 = "abc"
result = itertools.zip_longest(str1, str2)
print(list(result)) 
result = itertools.zip_longest(str1, str2,fillvalue=5)
print(list(result)) 