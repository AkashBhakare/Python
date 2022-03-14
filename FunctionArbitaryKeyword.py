# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:20:05 2021

@author: Akash
"""

#The Arguments are passed a dictionary and these
#arguments make a dictionary inside function with name
#Same as the parameter excluding double asterisk **

def print_arguments(**kwargs):
    print(kwargs)
    print(f"Data type of arguments: {type(kwargs)}")
    
def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")
        
if __name__ == '__main__':
    
    print_arguments( Country = "India",
                    Capital  = "New Delhi")
    
    intro(FirstName = "Sita",
          LastName  = "Patil",
          age       = 22,
          Phone     = 7083374923)
    
    intro(FirstName = "Akash",
          LastName  = "Bhakare",
          Email     = "akashbhakare2050@gmail.com",
          Country   = "India",
          Age       = 21,
          Phone     = 7083374923)
    
    
    
    d = intro(FirstName = "Akash",
          LastName  = "Bhakare",
          Email     = "akashbhakare2050@gmail.com",
          Country   = "India",
          Age       = 21,
          Phone     = 7083374923)
    
    
    intro(**d)
    


























