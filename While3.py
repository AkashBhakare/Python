# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:29:07 2021

@author: Akash
"""

## Controlling a Loop with User Confirmation
## Accept two integers and display their addition. Continue till user wishes

continueLoop = 'Y'
while continueLoop.upper() == 'Y':
    num1 = int(input("Enter the first integer : "))
    num2 = int(input("Enter the Second integer : "))
    print(num1,"+",num2,"=",(num1+num2))
    continueLoop = input("Do you want to continue(Y/N)? : ")
else:
    print("The End!")

