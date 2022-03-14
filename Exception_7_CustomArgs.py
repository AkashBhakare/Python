# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:14:26 2021

@author: Akash
"""

# BaseException: Common base class for all exceptions
class MyException(Exception):
    pass

class NonPositiveIntegerError(MyException):
    
    def __init__(self, x, y):
        
        super(NonPositiveIntegerError, self).__init__()
        
        if x<=0 and y<=0:
            self.msg = f'Both parameters are negative: {x}, {y}'
        elif x<=0:
            self.msg = f'first parameter is nagative: {x}'
        elif y<=0:
            self.msg = f'second parameter is negative: {y}'
            
    def __str__(self):
            return f"Error in function {self.name}: {self.msg}"
        
def average(x, y):
    try:
        if x <= 0 or y <= 0:
            raise NonPositiveIntegerError(x, y,average.__name__)
    except NonPositiveIntegerError as e:
        print(f"Inside inner try/except block!\n{e}")
        raise #re-raise
    else:
        return (x+y)/2
    
def division(x,y):
    try:
        if x <= 0 or y <= 0:
            raise NonPositiveIntegerError(x,y,division.__name__)
    except NonPositiveIntegerError as e:
        print(f"Inside inner try/except block!\n{e}")
        raise #re-raise
    else:
        return (x/y)
        
    
if __name__ == '__main__':
    try:
        result = average(8, 7)
        print(f"Average is : {result}")
        result = division(8, 7)
        print(f"Average is : {result}")
    except MyException as e:
        print(f"Handled in outer try {e}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        