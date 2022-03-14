# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:02:29 2021

@author: Akash
"""

# File Attributes

# Open a file
fo = open("B:\\Python_Impetus_Code\\abc.txt", "r")
print ("Name of the file: ", fo.name)
print ("Opening mode : ", fo.mode)
print ("File no : ", fo.fileno())
print ("Closed ? : ", fo.closed)
fo.close()
print ("Closed ? : ", fo.closed)

import sys
print ("stdout fileno : ",sys.stdout.fileno.__doc__)

