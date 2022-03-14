# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:46:49 2021

@author: Akash
"""

# Simple Decorator : 
#       decorators wrap a function, modifying its behavior.

def my_decorator(func):
    ''' I am a decorator '''
    
    def wrapper():
        ''' I am a wrapper '''
        print("Before \"",func.__name__,"\" is called.")
        func()
        print("After \"", func.__name__,"\" is called.")
        
    return wrapper

def sayHello():
    ''' I am a saying Hello '''
    print("Hello !")
    

@my_decorator
def sayWhee():
    ''' I am saying whee ''' 
    print("Whee!")

if __name__ == '__main__':
    
      sayHello = my_decorator(sayHello)
      sayHello()
      print(sayHello.__name__)

## Using Decorator
sayWhee()
    