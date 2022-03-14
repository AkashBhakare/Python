# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:33:57 2021

@author: Akash
"""

# Understanding scope of globally defined variable
globalVar = 10

def f1():
    # Cannot access local variable before assignment
    # print("Local Variable :",localVar)
    localVar = 99 # local to f1()
    print("Local Variable :",localVar)
    # We can access variable defiend globally inside 
    # a function
    print("Global Variable in f1 :",globalVar)
    

if __name__ ==  '__main__':
    print("Global in main",globalVar)
    # print("Local Variable of f1",localVar)
    f1()
    print("Global in main",globalVar)
    f1()
    globalVar = 100
    f1()
    print("Global in main",globalVar)
    
    # print(localVar) # Out of scope, so this gives an error
