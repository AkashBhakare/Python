# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:38:40 2021

@author: Akash
"""

#Iterators 

# We use for statement for lopping over a list.
print('Iterating over list')
for element in [1, 2, 3, 4]:
    print(element)
    
# If we use it with a string, it loops over its characters.
print('Iterating over characters in the String')
for char in "python":
    print(char)
    
# If we use it with a dictionary, it loops over its keys.
print('Íterating over characters in the string')
for k in {"x": 1, "y": 2}:
    print(k)
    
playerDict = {'Sachin':101,'Saurav':48,'Rahul':65}

for name,centuries in playerDict.items():
    print(f'{name} has scored {centuries} centiries')

# If we use it with a file, it loops over lines of the fill.
   
print('Iterating over lines in the file')
for line in open("dataiter.txt"):
   print(line,end="")
        
        
player_list = ['Sachin','Saurav','Rahul','Anil','Javagal']
print('list of player_list (using for loop1:')
for player in player_list:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    