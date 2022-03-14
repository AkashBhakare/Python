# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:34:15 2021

@author: Akash
"""

globalVar = 10 ## Global Variable

def f1():
    localVar = 99 
    print('global Inside f1',globalVar) ## Global Variable
    print('Local Inside f1',localVar) ## Local Variable

def f2():
    globalVar = 'A' ## Local Variable
    localVar = 100 ## Local Variable
    print('Inside f2',globalVar) ## Local Variable
    print('Inside f2',localVar) ## Local Variable

#You can bind a local variable in the global scope. 
#You can also create a variable in a function
#and use it outside the function.
#To do either, use a global statement   
    
x = 1 ## Global Variable
def increase():
    global x  #Binds the global variable to local scope
    global y  #Creates a global variable inside a function
    global globalVar
    print("Inside increase globalVar = ",globalVar)
    globalVar = 999
    print("Inside increase globalVar = ",globalVar)
    x = x + 1
    print("Inside increase X = ",x)
    x = 88
    y = 99
    print("Inside increase X=", x) 
    print("Inside increase Y=", y) 

if __name__ ==  '__main__':
    # f1()
    # print("Inside main",globalVar) ## Global Variable
    # print(localVar) # Out of scope, so this gives an error

    # f2()
    # print("Inside main",globalVar)
    
    increase()
    print("Inside main X=", x)
    print("Inside main Y=", y) 
    print("Inside main",globalVar)
