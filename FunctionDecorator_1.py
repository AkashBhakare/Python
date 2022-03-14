# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:31:55 2021

@author: Akash
"""


# Decorator without Argument

def capitalize(func):
    
  def uppercase():
    result = func()
    return result.upper()

  return uppercase


# @capitalize decorator takes in a callable(say_hello) 
# as an argument and returns another callable(uppercase).
@capitalize
def say_hello():
  return "hello"


#old_Hello = say_hello
say_hello = capitalize(say_hello)

if __name__ =='__main__':
#    The decorator modifies the say_hello function by 
#    changing its result to uppercase.
    print(say_hello())	# 'HELLO'