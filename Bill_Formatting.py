# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 16:46:16 2021

@author: Akash
"""

product = [ 
             {"name": 'Books   \t',   "price" : 49.95},
             {"name": 'Computer\t',   "price" : 579.99},
             {"name": 'Monitor \t',   "price" : 124.89}
             ]
line = '*'*30
print(line)
line = '='*30
print(line)
record = [{"\tCoding Temple, Inc"},
          {"\t283 Franklin St."},
          {"\tBoston, MA"}
          ]
format_string = "%(name)-7s  %(price)10.2f"
total_price = 0
for record in product:
    print(format_string % record)
    total_price += record["price"]

format_string = "%-7s  %10.2f"
print(line)
print(format_string % ("\t Total\n" ,total_price))
print(line)
line = '='*30

print("Thanks for Shopping us today!\n")

line = '*'*30
print(line)






