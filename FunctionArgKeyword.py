# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:17:16 2021

@author: Akash
"""

## Function to calculate the Simple Interest

def getSimpleInterest(principleAmt:float,interestRate:float,years:float)->float:
    return (principleAmt * interestRate * years)/100

interest = getSimpleInterest(1000,10,2)
print("Simple interest is Rs",interest)

interest = getSimpleInterest(2, 1000,10)
print("Simple interest is Rs",interest)

interest = getSimpleInterest(10,2,1000)
print("Simple interest is Rs",interest)

# 3 keyword Arguments in order
interest = getSimpleInterest(principleAmt=1000,interestRate=10,years=2)
print("Simple interest is Rs",interest)



# 3 keyword Arguments out of  order
interest = getSimpleInterest(interestRate=10,years=2,principleAmt=1000)
print("Simple interest is Rs",interest)



#Error Since Positional argument cannot follow keyword
interest = getSimpleInterest(principleAmt=1000,10,years=2)
print("Simple interest is Rs",interest)



