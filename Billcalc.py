# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:58:38 2021

@author: Akash
"""

# Calculate the gross bill amount given product rate and quantity purchased
# Gross Bill Amount = product rate X quantity purchased
import sys

# product_rate        = input('Enter the product Rate (Rs) : ')
# if not isinstance(float(product_rate),float):
#     print("Invalid product rate entered",file=sys.stderr)
#     sys.exit(0)
   
# product_rate = float(product_rate)
# quantity_purchased  = float(input('Enter Quantity Purchased : '))
# gross_bill_amount   = product_rate * quantity_purchased
# print(f"The Gross bill amount is {gross_bill_amount:.0f}")


# Graceful exit
def get_product_rate():
    product_rate = input('Enter the product Rate (Rs) : ')
    try:
        product_rate = float(product_rate)
    except ValueError as err:
        print("Product rate entered in wrong format",file=sys.stderr)
        print(err,file=sys.stderr)
        sys.exit(0)
   
    return product_rate
   
# give the program a chance to continue by recovering from error    
def get_product_price():
    while(True):
        try:
            product_price = input('Enter the product Rate (Rs) : ') 
            product_price = float(product_price)
            # Business rule is voileted
            if product_price < 0:
                raise ValueError('Product Price should be non-zero Positive value')
            break
        except ValueError as err:
            print("Invalid Product Price entered ",file=sys.stderr)
            print(err,file=sys.stderr)
            
    return product_price     
   
# # give the program a chance to continue by recovering from error    
def get_product_cost():
    import sys
    import typing
    from typing import Final
    
    MAX_ATTEMPTS:Final[int] = 3
    attempt_counter = 1
    
    while(attempt_counter <= MAX_ATTEMPTS):
        try:
            product_price = input('Enter the product Rate (Rs) : ')
            product_price = float(product_price)
            # Business rule is voileted
            if product_price < 0:
                raise ValueError('Product Price should be non-zero Positive value')
            break
        except ValueError as err:
            print("Invalid Product Price entered ",file=sys.stderr)
            print(err,file=sys.stderr)
        print()
        attempt_counter += 1  
    else:
        print("Sorry! Maximum Attempts exhausted",file=sys.stderr)
        print("Try again later",file=sys.stderr)
        sys.exit(0)
        
    return product_price          


if __name__ =='__main__':
    
    product_rate = get_product_rate()
    product_rate = get_product_price()
    product_rate = get_product_cost()
    
    print(f"Product Rate is Rs : {product_rate:.2f}")
    
    #quantity_purchased = get_quantity_purchased()
    #gross_bill_amount = calculate_gross_bill_amount(product_rate,quantity_purchased)
    #print(f"The Gross Bill Amount is Rs : {gross_bill_amount} ")

