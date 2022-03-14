# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:20:15 2021

@author: Akash
"""

# Treating Object as function

class Person:
    
    def __init__(self, name):
        self.__name = name
        
    def get_name(self)->str:
        return self.__name
    
# Defining object of Class person
P = Person("Raju")
# Calling Object
P()