# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:31:50 2021

@author: Akash
"""

from functools import wraps

def logged(func):
    '''Decorator Logged that logs the Function Call'''
    @wraps(func)
    def with_logging(*args, **kwargs):
        '''Nested function inside decorator logged'''
        print(f"{func.__name__} was called")
        result = func(*args, **kwargs)
        return result
    
    return with_logging

@logged 
def square(X):
    """returns the square of the argument passed"""
    return X * X


square = logged(square)

@logged
def foo():
    print("I am in foo")

foo = logged(foo)


if __name__ == '__main__':
    friendList = list()
    f(10)