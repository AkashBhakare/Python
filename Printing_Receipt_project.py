# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:31:55 2021

@author: Akash
"""
#Project-1 (Printing Receipt)

product = [ 
             {"name": '\tBooks   \t',   "price" :  49.95},
             {"name": '\tComputer\t',   "price" : 579.99},
             {"name": '\tMonitor \t',   "price" : 124.89}
             ]
line = '*'*35
print(line)
print("\tCoding Temple, Inc")
print("\t283 Franklin St.")
print("\tBoston, MA")
line = '='*35
print(line)
print("\tProduct Name" "\t" ,
      "Product Price")
format_string = "%(name)-1s \t$%(price)6.2f"

total_price = 0
for record in product:
    print(format_string % record)
    total_price += record["price"]

format_string = "%-6s\t\t\t\t\t$%6.2f"


print(line)
print(format_string % ("\t\t\t\t\tTotal\n" ,total_price))

print(line)
line = '='*35

print("\tThanks for Shopping us today!\n")

line = '*'*35
print(line)

















