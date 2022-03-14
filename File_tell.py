# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:30:42 2021

@author: Akash
"""

f = open("write.txt")
         
print(f.tell())
print(f.readline())
#print(f.tell())

f.seek(10)
print(f.readline())
print(f.readlines())
#print(f.tell())


f.close()