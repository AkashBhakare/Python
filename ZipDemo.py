# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:01:12 2021

@author: Akash
"""

fruits = ["Apple","Orange","Guava","Mango"]
price  = [123, 345, 123, 444, 232, 56, 45]

result = zip(fruits)

print(list(result))

print()
fruit_price = zip(fruits,price)
print(list(fruit_price))

qty = [2, 4, 12, 35, 56, 3]
print()
result = zip(fruits,price,qty)
print(list(result))
print()
result = zip(price,qty,fruits)
print(list(result))

fruits = ["Apple","Orange","Guava","Mango"]
price  = [123, 345, 123, 444, 232, 56, 45]

#zip both arguments
fruit_price = zip(fruits,price)
print(list(fruit_price))
#unzip
first,second=zip(*fruit_price)
print(first)
print(second)
