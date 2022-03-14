# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:19:12 2021

@author: Akash
"""



glb_var = "Hi!, i'am global"
state   = "Hi I am global state"

# Closure : Non Local

def tester(start):
    state = start # Each call gets its own state
    state = state + 1
    
    
    def nested(label):
        # Nonlocals must already exist in enclosing def!
        nonlocal state # Remembers state in enclosing scope
        print(f"{label}, {state},{start}, {glb_var}") 
        # Allowed to change it if nonlocal  
        state += 1 
    
    return nested

if __name__ == '__main__':
    getting = tester(5)
    getting("First")
    getting("Second")
    getting("Third")
      
    
    print(getting.__closure__)
    print(type(getting.__closure__))  #tuple
    print(type(getting.__closure__[0])) #tuple::cell
    print(type(getting.__closure__[0].cell_contents)) #tuple::cell::int
    
    print(type(getting.__closure__[0].cell_contents)) #start
    print(type(getting.__closure__[1].cell_contents)) #state
    
    
    #Number of variables of the surroundion scope that the nested function is
    print(f"Number : {len(getting.__closure__)}")
    
  
    getting("Hello")
    print(getting.__closure__[0].cell_contents)
    print(getting.__closure__[1].cell_contents)
    
    
    getting("Hi")
    print(getting.__closure__[0].cell_contents)
    print(getting.__closure__[1].cell_contents) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
