# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:20:59 2021

@author: Akash
"""

# understanding the helper function Enumerate

S = 'impetus'
for item in S:
    print("\'",item,"\'",sep = '')



# traditional way to maintain offset
print('Using counter with for loop') 
S = 'impetus'
offset = 0
for item in S:
    print("\'",item,"\'",' appears at offset ', offset, sep='')
    offset += 1

# maintaining offset using enumerate function
print('Using enumerate with for loop')
S = 'TIGER'
for (offset, item) in enumerate(S):
    print("\'",item,"\'", 'appears at offset', offset)

# using enumerate to get offset of elements in list
players = ['Sachin','Saurav','Rahul','Vinod']
for (offset,item) in enumerate(players):
    print( offset+1,")Name = ",item,sep='')

# using enumerate to get offset of elements in list
players = ['Sachin','Saurav','Rahul','Vinod']
for (offset,item) in enumerate(players,start =1):
    print( offset,")Name = ",item,sep='')
    
# get enumerate object
print("Enumerate returns:\n",enumerate(players))

# pass the enumerate object to list ctor
# to get list of tuples containing (offset,item)
result = list(enumerate(players))
print("Elements\n:",result) # prints list of tuples

result = list(enumerate(players,start=1))
print("Elements\n:",result) # prints list of tuples

eobj = enumerate(players)
print("Element = ",eobj.__next__()) # returns next tuple
print("Element = ",eobj.__next__())
print("Element = ",eobj.__next__())
print("Element = ",eobj.__next__())


