# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:33:15 2021

@author: Akash
"""

# Formula:- [ (p*(1+r/100)^n)-p]

def getCompoundInterest(principleAmt:float,interestRate:float,years:float)->float:
    return (principleAmt * (1+ (interestRate/100))**years)-principleAmt

#positional arguments
p_amount = 1000
roi  = 10
years = 2


ci = getCompoundInterest(1000, 10, 2)
print(f"Compund interest is Rs {ci:.2f}")
ci = getCompoundInterest(p_amount, roi, years)
print(f"Compund interest is Rs {ci:.2f}")


ci = getCompoundInterest(2, 10, 1000)
print(f"Compund interest is Rs {ci:.2f}")
ci = getCompoundInterest(years, roi, p_amount)
print(f"Compund interest is Rs {ci:.2f}")

#Keyword Arguments
ci = getCompoundInterest(years=2, principleAmt=10, interestRate=1000)
print(f"Compund interest is Rs {ci:.2g}")
ci = getCompoundInterest(years=2, principleAmt=p_amount, interestRate=roi)
print(f"Compund interest is Rs {ci:.2f}")



ci = getCompoundInterest(interestRate=1000,years=2, principleAmt=10)
print(f"Compund interest is Rs {ci:.2f}")

