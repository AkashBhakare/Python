# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:58:27 2021

@author: Akash
"""



from typing import Final 
MIN_AGE :Final = 18
MAX_AGE :Final = 60

age = int(input("Whats your age in years?"))

# if (age >= MIN_AGE and age <= MAX_AGE):
#     print("You are eligible to work")
# else:
#     print("You are not eligible to work")

# Alternative
MIN_AGE :Final = 18
MAX_AGE :Final = 60
if ( MIN_AGE <= age <= MAX_AGE):
    print("You are eligible tio work")
else:
    print("You are not eligible to work")
    
