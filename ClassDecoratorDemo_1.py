# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 15:44:35 2022

@author: Akash
"""

# Uderstand the class method decorator
# this example highlight the difference between 
# the instance method and class method

class sample(object):
    
    class_data = 99  # shared between all object of the class
    
    def __init__(self):
        self.instance_data = 10
        
    def foo(self):  #instance method
        print('Inside foo')
        print('Instance data = ', self.instance_data)
        print('Class data = ', self.class_data)
        print('I am ', self)
        
    @classmethod 
    def baz(cls):
        print('Inside baz')
        print('Instance data = ',cls.instance_data)
        print('Class data = ', cls.class_data)
        print('I am ', cls)
        
    @staticmethod 
    def bar(msg):
        print('Inside bar')
        #print('Instance data = ', instance_data)
        #print('Class data = ', cls.class_data)
        print('bar says', msg)
        


if __name__ == '__main__':

# instance methods
   # Sample.foo()  # Error
   s = sample()
   s.foo() # Invoke the instance method
    
#class methods
   s.baz() # Class meethod invoked using object
   sample.baz()  # class method invoked using class
   
# Static method
   s.bar("hello")
   sample.bar("bye")
   
             


    




















