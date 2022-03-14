# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:29:54 2021

@author: Akash
"""

def capitalize(func):
    
  def uppercase(*args):
    result = func(*args)
    return result.upper()

  return uppercase

# say_hello = capitalize(say_hello)
# say_hello = uppercase
# say_hello = ('Rutuja')

@capitalize
def say_hello(name:str):
    return f'hello!, {name}'

def squareit(func):
    
    def wrapper(*args):
        # print("Function actually called is :",wrapper.__name__)
        # print("Name of the function wrapped :",func.__name__) 
        result = func(*args)
        return result ** 2
    return wrapper

@squareit 
def doit(data:int):
    return int(str(data)[::-1])


@squareit 
def addition(*args):
    return sum(args)


#Decorating the predefined function
def mydeco(func):
    def myprint(*args):
        func('Started printing')
        for arg in args:
            func(f"**{args}**")
        func('Finished Printing')
        
    return myprint 

if __name__ == '__main__':
    result = say_hello('mangesh')
    print(result)
    
    print(addition.__name__)
    print(addition(3,4))
    print(addition(3,4,5))
    
    #passing predefined function to decorater
    print = mydeco(print)
    
    print("First")  #modified function is called
    print("first","Second","Third")
    del print 
    print("Second")  # reverted to original behavior
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


