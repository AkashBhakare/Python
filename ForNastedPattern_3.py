# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:29:23 2021

@author: Akash
"""
# 1
# 1 2
# 1 2 3
# 1 2 3 4

total_rows = int(input("Please enter the number of rows :"))

for row in range(1,total_rows+1):
    print()
    for col in range(1, row+1):
        print(col," ",end=" ")
        
#              *
#           *      *
#        *     *       *
#    *      *      *       *
for row in range(1,total_rows+1):
    print()
#print space before the star's are printed on any row
    for col in range(1, (total_rows-row)+1):
        print(" ",end="")
# print star on every row       
    for col in range(1, row+1):
        print("* ",end="")
        
              #   1
              #   0 1
              #   1 0 1
              #   0 1 0 1

          
          #    *
          #   ***
          #  *****
          # ******* 
print("\n\n")          
for row in range(1,total_rows+1):
    print()
#print space before the star's are printed on any row
    for col in range(1, (total_rows-row)+1):
        print(" ",end="")
# print star on every row       
    for col in range(1, 2*row):
        print("*",end="")
        
        
          # *******
          #  *****
          #   ***
          #    *
        
        
        # 4 3 2 1
        # 4 3 2 
        # 4 3
        # 4
        
        
        # 1  2  3  4
        # 5  6  7 
        # 8  9 
        # 10
    