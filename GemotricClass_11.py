# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:43:03 2021

@author: Akash
"""

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "\n\tcolor: " + self.__color + \
            " \n\tfilled: " + str(self.__filled)
    
    
    
    
    
    def getArea(self):
        raise NotImplementedError
        
    def getPerimeter(self):
        raise NotImplementedError