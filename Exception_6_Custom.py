# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:50:15 2021

@author: Akash
"""

# Common base class for all non-exit exception.
class MyException(Exception):
    pass

class NonPositiveIntegerError(MyException):
    pass

class NonPositiveIntegerError(MyException):
    pass

def TooBigintegerError(MyException):
    pass

def average(x:int, y:int)->float:
    if not isinstance(x,int):
        raise TypeError("first parameter has to be of type int")
        
    if x <= 0 or y <= 0:
       raise NonPositiveIntegerError('Either of the parameter is not positive')
    
       
    if x > 10 or y > 10:
        raise TooBigintegerError('Either of the parameter too large')
        
    return (x+y) / 2

if __name__ == '__main__':
    try:
        # print("The Avarage is :",average('a', 'b'))
        # print("The Avarage is :",average(-1, -1))
        # print("The Avarage is :",average(100, 400))
        # print("The Avarage is :",average(10, 4))
        
         print("The Avarage is :",average(119, 10))
    
    # except (NonPositiveIntegerError,TooBigintegerError) as e:
    #     print(f"1:) {e}")
    except MyException as e:
        print(f"2:) {e}")
    except TypeError as te:
        print(f"3:) {te}")
    else:
        print("Got the Average!")
    finally:
        print("Visited finally")
    
    print('Done')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        