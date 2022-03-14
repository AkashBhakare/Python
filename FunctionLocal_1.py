# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:10:15 2021

@author: Akash
"""

def temperature(degCel:float)->str:
    '''
    parameters
    degCel : float
        Takes the temperature in Degree celcius are a single parameter.
        
    Returns
    --------
    str
       RFeturns the temperature in Farenheit
       
    '''
    
    #Local : Helper Function
    def celcius2fahrenheit(deg:float)->float:
           return deg * (9 / 5) + 32
    Farenheit = celcius2fahrenheit(degCel)
    return f" It's {Farenheit} degree Farenheit!"


if __name__ == '__main__':
    tempCel = float(input("Enter temperature in degree Celcius : "))
    results = temperature(tempCel)
    