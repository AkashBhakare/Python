# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:58:00 2021

@author: Akash
"""

# Find the longest string

def findlongest(*args):
    maxLen = 0
    maxStr = None
  # print(args)
    for element in args:
        if len(element) > maxLen:
            maxLen,maxStr = len(element),element
    
  
    return maxStr
    
if __name__ == '__main__':
    var = findlongest("a","bb","ccc","dddddd","eee")
    print(var)
    print(findlongest("a","bb","ccc","dddddd","eee"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
  
  