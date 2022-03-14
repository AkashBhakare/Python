# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:20:48 2021

@author: Akash
"""


# Functions Can Be Passed To Other Functions

def yell(text):
    return f"text.upper() +!!"

def greeting(name:str)->str:
    return f"Hello {name} Good Morning"

def call(func, text:str)->None:
    message = func(text)  #indirect Call
    print(message)
    
    
if __name__ == '__main__':
    #Userdefined function as first parameter
    call(yell,"Shraddha")
    call(greeting,"Shraddha")
    
    #predefined function as first parameter
    call(str.lower,"AKASH")
    call(str.capitalize,"AKASH")
