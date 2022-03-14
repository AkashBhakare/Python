# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:33:35 2021

@author: Akash
"""

# Scope of Global Variables

import random

# Global Variables
lucky_number = random.randint(0,100)
name         = 'Hrishi'


def f1():
    print(f"{name}'s Lucky Number in f1 = {lucky_number}")
   
    return
    

def f2():
    print(f"{name}'s Lucky Number in f2 = {lucky_number}")
  
    return
    

def f3():
    name         =  "Sandesh"               # Local to f3
    lucky_number = random.randint(0,100)    # Local to f3
    print(f"{name}'s Lucky Number in f3 = {lucky_number}")
   
    return

def f4():
    # Cannot access local varaibles before they are assigned value
    # print(f"{name}'s Lucky Number in f4 = {lucky_number}")
    #Assignment creates a new local variable that hides the global variable
    name         =  "Ali"                   # Local to f4
    lucky_number = random.randint(0,100)    # Local to f4
    print(f"{name}'s Lucky Number in f4 = {lucky_number}")
    return



def f5():
    #Need to declare global variable in function if they are to be assigned 
    global name
    global lucky_number
    print(f"{name}'s Lucky Number in f5 = {lucky_number}")
    #Following assignment will affect global variable
    name         =  "Chhaya"               # Global varaible
    lucky_number = random.randint(0,100)   # Global varaible
    print(f"{name}'s Lucky Number in f5 = {lucky_number}")
    return

    
if __name__ == '__main__':
      f1()
      f2()
      print(f"{name}'s Lucky Number in main = {lucky_number}")
   
      f3()
      print(f"{name}'s Lucky Number in main = {lucky_number}")
  
      f4()
      print(f"{name}'s Lucky Number in main = {lucky_number}")
      f5()
      print(f"{name}'s Lucky Number in main = {lucky_number}")
    
