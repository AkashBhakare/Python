# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 08:58:06 2021

@author: Akash
"""
def print_table(number:int)->None:
    for count in range(1,11):
        print(f"{number:2} x {count:2} ={number*count:3}")   

print_table(8)