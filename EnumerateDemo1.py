# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:20:42 2021

@author: Akash
"""


grocery = ['bread', 'milk', 'butter', 'egg']


for item in grocery:
    print(item)
    

index =  1
for item in grocery:
    print(index,") ",item,sep='')
    index += 1


print()

for item in enumerate(grocery):  	
    print(item)

print()

for count, item in enumerate(grocery):  	
    print(count, item)

print()

for count, item in enumerate(grocery,start=1):  
    print(count,") ", item,sep='')


string = "IMPETUS"
for index, letter in enumerate(string,start=1):
    print(index,". ", letter,sep="")




data = enumerate(grocery)
print(type(data))
print(next(data))





import itertools
# This function cycles through an iterator endlessly.
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
data = enumerate(itertools.cycle(colors),start=1)
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
print(next(data))

