# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:48:47 2021

@author: Akash
"""

def flip_coins(file_name:str):
    for line in open(file_name):
        h_count = 0
        t_count = 0
        for char in line:
            if char.lower() in ['h','head']:
                h_count = h_count + 1
            elif char.lower() in ['t','tail']:
                t_count = t_count + 1
            percentage = (h_count/(h_count+t_count)*100)
            if percentage > 50:
                print(f"{h_count} heads {percentage:.0f})")
                print("There were more heads!\n")
            else:
                print(f"{h_count} heads {percentage:.0f})\n")
                

if __name_ == "__main__":
    flip_coins("C:\Users\Akash\FH_ASSI_Flip_coins.txt")
                