# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:34:03 2021

@author: Akash
"""

# num1 = int(input("Please enter First integer :"))
# num2 = int(input("Please enter second integer :"))
# if num1 > num2:
#     max_num = num1
# else:
#     max_num = num2
# print("Maximum number is ",max_num)

num1 = 90
num2 = 100
#print("Max is ", num1 if (num1 > num2) else num2 )

# max_num = (num1 if num1 > num2 else num2)
# print("Max =",max_num)

max_num = (num2, num1) [num1>num2]
print("Max = ",max_num)