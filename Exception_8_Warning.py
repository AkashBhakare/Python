# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:34:03 2021

@author: Akash
"""

import warnings
 
def basic_warn1():
    print('Before the warning')
    warnings.warn('This is a warning message')
    # raise Exception("some Error!")
    print( 'After the warning')

def basic_warn2():
    import math
    n = 5
    result = math.factorial(n)
    print(f"Factorial of {n} = {result}")
    n = 4
    try:
        result = math.factorial(n)
        print(f"Factorial of {n} = {result}")
    except TypeError:
        print("Invalid type of input supplied!\n")
    

def filter_demo():
    warnings.filterwarnings('ignore', '.*do not.*',)
    warnings.filterwarnings('ignore', '.*show.*',)
    print('Before the warning')
    warnings.warn('Show this first warning message')
    warnings.warn('DO Not show this message')
    warnings.warn('Show this last last message')
    warnings.warn('This is the very last message')
    print( 'After the warning')


# python -W "ignore:do not:UserWarning::0" demo.py
    
def warn_error():
    # This filter tells the warnings module to raise an exception when the 
    # warning is issued.
    # warnings.simplefilter(action='default', category=UserWarning,lineno=0)
    # warnings.simplefilter(action='ignore', category=UserWarning,lineno=0)
    # warnings.simplefilter(action='ignore', category=UserWarning,lineno=50)
    # warnings.simplefilter(action='module', category=UserWarning,lineno=10)
    # warnings.simplefilter(action='default', category=RuntimeWarning)
    print('Before the warning')
    warnings.warn(message='This is a user message')
    warnings.warn(message='This is another user warning message',category=UserWarning)
    warnings.warn(message='This is a DW warning message',category=DeprecationWarning)
    warnings.warn(message='This is a RW warning message',category=RuntimeWarning)
    warnings.warn(message='This is a user message')
    print( 'After the warning')
    # to control from command prompt 
    
# python -W "error::UserWarning::0" warn_demo.py
# python -W "ignore::UserWarning::0" Exception_8_Warning.py


print("That's all folks!")
    


if __name__ == '__main__':
     basic_warn1()
     basic_warn2()
     filter_demo()
     warn_error()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    