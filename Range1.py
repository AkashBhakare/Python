# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:11:16 2021

@author: Akash
"""

# iterate through 0..10
for counter in range(11):
    print(counter)
    
 # iterate through 1..10
for counter in range(1,11):
    print(counter)   

 # iterate through odd numbers between 1..10
for counter in range(1,11,2):
    print(counter)  
     
# iterate through Even numbers between 1..10
for counter in range(2,11,2):
    print(counter) 

#iterate in descending order
for counter in range(10,0,-1):
    print(counter)    
    
#iterate in descending order only Even numbers between 10..1
for counter in range(10,0,-2):
    print(counter)  
   
for element in range ('a', 'z'):
    print (element)
    
start   = ord('A')
stop    = ord('Z')+1
print(start,stop) 
for element in range (start,stop):
    print (chr(element))    
    
