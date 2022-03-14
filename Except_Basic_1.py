# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:32:08 2021

@author: Akash
"""

## Handling Exception (Basic)

import sys

def getInteger(msg:str)->int:
    
    while(True):
        try:
            integer = int(input(msg))
            break
        except ValueError:
            print("You have given an invalid input!",file=sys.stderr)
    # end of the loop    
    
    return integer


def divide(numerator:int, denominator:int)->float:
  
    if (not isinstance(numerator, int)):
        raise TypeError(f"Numerator:'{numerator}' supplied is not of Integer Type!")
        
    if (not isinstance(denominator, int)):
        raise TypeError(f"Denominator:'{denominator}' supplied is not of Integer Type!")    
    
    if (denominator == 0):
        raise ZeroDivisionError("Denominator should not be Zero!")
   
    return numerator/ denominator

if __name__ == '__main__':
    print("Hello")
    try:
        numerator   = getInteger("Please enter Numerator : integer in digits:")
        denominator = getInteger("Please enter Denominator : Integer in digits:")
##        print(numerator/ denominator)
##        
        result      = divide(numerator, denominator)
        print(f"{numerator} / {denominator} = {result}")
##        
        numerator   = "Ten"
        denominator = "Five"
        result      = divide(numerator,denominator)
        print(f"{numerator} / {denominator} = {result}")
        
    # Raised when an operation
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except Exception:
        print("Unknown Error")
    finally:
        print("All Over!")
