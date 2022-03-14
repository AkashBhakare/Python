# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:44:14 2021

@author: Akash
"""

## Accept SAARC country name and display its capital
## Stop only when user enters "Exit" as country name

##SAARC = {
##  "India": "New Delhi",
##  "Bangladesh": "Dhaka",
##  "Pakistan": "Islamabad",
##  "Nepal":"Kathmandu",
##  "Bhutan":"Thimpu",
##  "Maldives":"Male",
##  "Sri Lanka":"Colombo",
##  "Afganistan":"Kabul"
##}

SAARC = dict(India="New Delhi", Bangladesh="Dhaka",Pakistan="Islamabad",
  Nepal="Kathmandu",Bhutan="Thimpu", Maldives="Male",SriLanka="Colombo",
  Afganistan="Kabul")

while True:
    country = input("Enter SAARC country name (Or Type \'exit\' to stop) :")
    if country.upper() == "EXIT":
        break
    
    if country.title() in SAARC:
        print("Capital city of ",country ,"is",SAARC.get(country))
    else:
        print("Not a SAARC Country name")
        
        
