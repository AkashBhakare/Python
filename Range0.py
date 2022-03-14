# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:05:57 2021

@author: Akash
"""

# understanding range():
# a built-in that generates successive integers

my_range = range(5)
print("type :", type(my_range))
print("range object :", my_range)

# Access range elements
number = my_range[0]
print("element at first position :",number)
number = my_range[-1]
print("element at last position :",number)

my_list = list(my_range)
print("List:", my_list)

#range attributes
numbers = range(20)
numbers = range(5, 20)
numbers = range(5, 20, 2)
print("Start    :", numbers.start)
print("Stop     :", numbers.stop)
print("Step     :", numbers.step)
print("Range    :", list(numbers))

numbers.start = 8 #Error since range attributes are readonly 

myrange = range(-numbers.start, -numbers.stop, -numbers.step)
print(myrange)
print("Start    :", myrange.start)
print("Stop     :", myrange.stop)
print("Step     :", myrange.step)
print("Range    :", list(myrange))


myrange = range(-5, -20, -1)
print("Range    :", list(myrange))

# generate numbers in the range of 0-4
myList = list(range(5))
print('List  :', myList)

# generate numbers in ascending order from -5 to 4 step 2
myList = list(range(-5,5,2))
print('List  :', myList)

#generate numbers in descending order from 5 to -4
myList = list(range(5,-5,-1))
print('List  :',myList)

#Containment
myrange = range(5)
print("myrange :", list(range(5)))
print("4 in range ? ", 4 in my_range)
print("4 not in range ? ", 4 not in my_range)
print("7 in range ? ", 7 in my_range)
print("7 not in range ? ", 7 not in my_range)
