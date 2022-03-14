# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:51:50 2021

@author: Akash
"""

# Recursive function

# Recursive function to compute factorial
def getFactorialRec(number):
    if number == 1:
        return 1
    else:
        return number * getFactorialRec(number - 1)

# Non-Recursive function to compute factorial
def getFactorialNonRec(number):
    f = 1
    while number != 1:
        f = f * number
        number = number - 1
    return f

        
if __name__ == '__main__':
    num = int(input("Enter a number:"))
    factorial = getFactorialRec(num)
    print("Factorial of", num , "=", factorial)
    num = int(input("Enter a number:"))
    factorial = getFactorialNonRec(num)
    print("Factorial of", num , "=", factorial)
  