# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:39:46 2021

@author: Akash
"""

## Accept alphabet from user and chaeck whether it is
## vowel or consonant. Contiue till user does not enter 'Z'

vowels = ['A','E','I','O','U']
MAX_LEN = 1
data = input("Enter an alphabet : ")

while data.upper() != 'Z' :
    if len(data) > MAX_LEN :
        print('Enter a Single alphabet')
    elif data.isalpha():
        if data.upper() in vowels:
            print("'",data,"' is a vowel")
        else:
            print("'",data,"' is a consonant")
    else:
        print("Invalid input!, Enter an alphabet (A-Z)")
    data = input("Enter another alphabet : ")
else:
    print("The End !")
        
