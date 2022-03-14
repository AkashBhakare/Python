# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:19:58 2021

@author: Akash
"""

# Function Object -- Indirect Function Call

# Name echo assigned to function object
def show(message:str)->None:
    '''Simple Function to eacho the content passed'''
    print(message.capitalize())


if __name__ =='__main__':
    # Call object through original name
    show('Direct call')
    
    # Now x references the function too
    display = show
    # Call object through name by adding ()
    display('Indirect call!') 
    
    #Function objects and their names are two separate concerns
    del show
    show('Direct call')  # Error; has been deleted
    display('Indirect call!')  # Still points to same function object 
    
    ## Attribute __name__
    print(display.__name__)
    print(show.__name__)
    print(display.__doc__)
    print(display)
    display.__name__ = "Echo_Message"
    print(display.__name__)
    
    print(show.__name__)
    print("New Message")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    