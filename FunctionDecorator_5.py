# -*- coding: utf-8 -*-

"""
Created on Wed Oct 13 11:58:36 2021

@author: Akash
"""

# Reusable Decorators

def do_twice(func):
    
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
     
    return wrapper_do_twice

# end of decorator do_twice

def debug(func):
    '''Print the function details '''
    
    def wrapper_debug(*args, **kwargs):
        print(f"Calling {func.__name__!r} with {(len(args)+len(kwargs))!r} arguments")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           
        return value
    
    return wrapper_debug

# end of decorator debug

@do_twice
@debug
def say_hello():
  print("hello")
  return "Bye"

say_hello() = debug(do_twice(say_hello))
#say_hello() = do_twice(debug(say_hello))

@do_twice
def say_hello(*args):
    for ele in args:
         print("Hello",ele)
    return "*"


@debug
def greet(*args):
    for ele in args:
         print(f"Hello{name}")
    return '*'


if __name__ =='__main__':
    say_hello()
    print( say_hello())
    say_hello("Dheeraj","Manish") #Error
    greet("Dheeraj","Manish")
    print(greet("Dheeraj","Manish")) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    