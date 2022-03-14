# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:25:38 2021

@author: Akash
"""
#Using Itertools

import itertools

# itertools.count(start=0, step=1)
# Makes an iterator that returns evenly spaced values
#starting with number start.

for i in itertools.count(10,3):
    print(i)
    if i > 20:
        break
    
# This function cycles though an iterator endlessly.
colors = ['red','orange','yellow','green','blue','violet']
for color in itertools.cycle(colors):
    print(color)
    
# itertools.permutations(iterable, r=None)
alpha_data = ['a','b','c']
result = itertools.parmutations(alpha_data)
for each in result:
    print(each)
    
# cartesian product from a series of iterables.
num_data = [1, 2, 3]
alpha_data = ['a', 'b', 'c']
result = itertools.product(num_data, alpha_data)
for each in result:
    print(each)
    
# This function will repet an object over and over again.
#Unless, there is a times argument.

for i in itertools.repeat("hello"):
    print(i)
    
for i in itertools.repeat("hello",3):
    print(i)
    
# This function allows you to cut out a piece of an iterable.
colors = ['red','orange','yello','green','blue',]
few_colors = itertools.islice(colors, 3)
for each in few_colors:
    print(each)




















