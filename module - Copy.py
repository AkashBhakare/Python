# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:56:18 2021

@author: Akash
"""

def print_table(number:int)->None:
    i=1
    while(i<=10):
        print(f"{number:2} x {i:2} ={number*i:3}")
        i+=1
    return;        
if __name__=='__main__':
	number = 4
	print(print_table(number))

























