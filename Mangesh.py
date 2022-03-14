# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:23:35 2021

@author: Akash
"""

import sys

def print_table(number:int)->None:
    """
    prints the table of an integer number taken as an argument by using the concept of generator expression. 

    """
    table_generator = (number * table for table in range(1,11))
    
    while True :
        try:
            print(f"{int(next(table_generator)):{len(str(number*10))}d}") 
        except StopIteration:
            print(f"The table of {number} is printed succesfully !") 
            break          
             
if __name__=="__main__":
    #number = input("Please enter the first number you want to print : ").strip()
    number = "3"
    if not number.isdigit():
        print("Please enter a valid number")
        sys.exit(0)
    else:  
        number = int(number)  
        print_table(number)