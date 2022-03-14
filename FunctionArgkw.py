# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:20:29 2021

@author: Akash
"""

# *args allow us to pass the variable number of 
# non keyword arguments to function
# Where ew have at least one required arguments
#In these instances, order maters. Positional-only parameters
#must come first, so args and **kwargs are placed after

# if we have one required argument:
def func1(required_arg, *args, **kwargs):
    print(f'''Required_arg                  :{required_arg}
Arbitary Positional Arguments: kwargs:''')

#If there are two required arguments:
def func2(required_arg1, required_arg2, *args,**kwargs ):
    pass

def one_required_arg(required_arg,*args, **kwargs):
    print(f"Required Args: {required_arg}")
    if args:
        print(f"Args : {args}")
    if kwargs:
        print(f"Kwargs: {kwargs}")

if __name__ == '__main__':
    print("First Call")
    func1()
    func1(1)
    func1(1, 2)
    func1(1, 2, 23)
    func1(1, 2, 3, 4, one=1, two=2)
    func1(1, *(2,3,4), one=1, two=2)
    
    
    func2(11,22)
    func2(11,22,33)
    func2(11,22,33,44)
    
    one_required_arg("Reqd_args")
    
    
    
#   print("\nSecond Call")
    one_required_arg("reqd_args", 1, 2, '3')
    
    
    print("\nThird Call")
    one_required_arg("reqd_args",
                     1, 2, '3',
                     state="Maharashtra", capital= "Mumbai")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    