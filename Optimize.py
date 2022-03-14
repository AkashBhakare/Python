# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:26:40 2021

@author: Akash
"""

a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl'
print(a is b)
print(a == b)
print(a is c+'d')
print(a == c+'d')

#As the string name is immutable:
#TypeError: 'str' object does not support item assignment
name = 'Wtack Abuse!'
name[0] = 'S'


#Note: If you really did want to change a particular character of a string, 
#you could convert the string into a mutable object like a list,
#and change the desired element:
name = 'Wtack Abuse!'
name = list(name)
name[0] = 'S'
# Converting back to string
name = "".join(name) 
print(name)


name = "Akash Bhakre!"
name = list(name)
name[10] = 'a'
name = ''.join(name)
print(name)


letter_d = 'd'
a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl' + letter_d
d = 'Hello Worl' + 'd'
print(f"The ID of a: {id(a)}")
print(f"The ID of b: {id(b)}")
print(f"The ID of c: {id(c)}")
print(f"The ID of d: {id(d)}")


#Implicit Interning
a = 'why'
b = 'why' * 5

B = "".join(['w','h','y'])
t ='Hello Worl' + letter_d 


#Explicit Interning
import sys
c = sys.intern('Hello World'+'!')

import sys
letter_d = 'd'

a = sys.intern('Hello World')
b = sys.intern('Hello Worl' + letter_d)
print(f"The ID of a: {id(a)}")
print(f"The ID of b: {id(b)}")
print(f"a is b? {a is b}")



