# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:43:44 2021

@author: Akash
"""

import warnings


# Cavets 1

def getBillAmount(product_rate, quantity_purchased):
        assert isinstance(product_rate,int), "Invalid format of product Rate"
        assert isinstance(quantity_purchased,int), "Invalid format of Quantity Purchased"
        return product_rate * quantity_purchased
    
# Cavets 2

def getDouble(num):
    assert (isinstance(num,int),"Incorrect data supplied")
    return num * 2

if __name__ == '__main__':
    # product_rate = 12
    # quantity_purchased = "Five"
    # bill_amount = getBillAmount(product_rate,quantity_purchased)
    # print("Bill Amount is Rs :",bill_amount)
    square = getDouble(10.5)
    print("Double = ",square)        