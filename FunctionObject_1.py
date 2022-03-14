# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:21:09 2021

@author: Akash
"""

# Function as Objects : 
# Functions Can Be Stored In Data Structures
# Attributes : __name__ , __doc__


def multiply(n1=1,n2=1):
    '''x'''
    return n1*n2

def add(n1=1,n2=1):
    '''+'''
    return n1+n2

def divide(n1=1,n2=1):
    '''/'''
    return n1/n2

def power(n1=1,n2=1):
    '''**'''
    return n1**n2



#Set/List of user defined Functions{}/[]
user_defined_function_set = {add, multiply, divide, power}

#List of Method(function) : prdefined
predefined_defined_method_list = [str.lower, str.capitalize, str.upper]

predefined_defined_function_tuple = (len,sum,max,min)

if __name__ == '__main__':
    #List the str method function in list
    for func in predefined_defined_method_list:
        print(func)
        
    #lists the predefine function stored in tuple  
    for func in predefined_defined_function_tuple:
         print(func)
         
    #list the userdefined functions functions stored in set
    for func in predefined_defined_function_tuple:
        print(func)
        
    #Lists the str method stored in list
    for func in predefined_defined_method_list:
        print(func.__name__)
    
    #Lists the predefined functions stored in tuple
    for func in predefined_defined_function_tuple:
         print(func.__name__)
    
    #Lists the userdefined function function stored in list
    for func in user_defined_function_set:
        print(f"{func.__name__} : {func('HEy tHEre')}")
        
    n1 = 10
    n2 = 7
    
    #Sets are unodered by default
    for afunction in predefined_defined_method_list:
        print(afunction(n1,n2))
        
    for afunction in user_defined_function_set:
        print( f'{n1} {afunction.__doc__:^3} {n2} = {afunction(n1,n2)}')
        
    for afunction in user_defined_function_set:
        print( f'{n1} {afunction.__doc__:^3} {n2} = {afunction(n1,n2)}'
        
#    for afunction in user_defined_function_set:
#       arg1, arg2 = afunction.__defaults__
#       print( f'{arg1:4} {afunction.__doc__:^2} {arg2:2} = {afunction()}'
#        print(res)
        
































