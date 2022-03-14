# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:22:27 2021

@author: Akash
"""


# make print_table function:
def print_table(number:int)->int:
    i=1
    while i<=10:
        print(f"{number:2} x{i:2} ={number*i:3}")
        i=i+1
if __name__=='__main__':
    #number=int(input("Which table do you want to print"))
    number = 3
    print_table(number)