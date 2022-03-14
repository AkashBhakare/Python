# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 16:27:59 2022

@author: Akash
"""

import time

class Date:
    # Primary Constructor
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day
        
        
    @classmethod 
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
    
    
    def __str__(self):
        return f"{self.__day}/{self.__month}/{self.__year}"
    
if __name__ == '__main__':
    #Explicit call to the constructor __init__
    d = Date(2022,1,1)
    print(d)
    
    
    # Factory for getting todays date
    t = Date.today()
    print(f"today :{t}" )
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    