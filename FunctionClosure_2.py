# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:09:59 2021

@author: Akash
"""


# Closure : Non Local
# Variables of the surrounding environment are read only
# when accessed in nested function without nonlocal declaration
glb_var = "hi!"

def tester(start):
    #Local varaibles of the oter enclosing function
    state = start 
    state = state + 1
    
    def nested(label):
      #Function can alter the value of its local variable
       label = label + 1
       print(f"{label}, {state},{start}, {glb_var}") 
       #Error: Varibles of surrounding scope are read only
       #inside the nested function
       #state = state + 1
       #start = start + 1
    
    return nested

if __name__ == '__main__':
    func1 = tester(0)
    print(func1.__name__)
    func1(9)
    
    
    func2 = tester("45.5")
    func2(0.5)
    func2(66)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
