# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:03:27 2021

@author: Akash
"""

class Circle:
    '''This class represent a Circle object and enable you to calculate the
    area and perimeter of the Circle in addition to setting and getting its radius'''
       
    def __init__(self, radius = 1)->None:
        '''
         Args:
            radius (TYPE: float, optional): Constructs a Circle object with given radius. 
            Defaults to 1.
        Returns:
            None

        '''
        if self.__isRadiusValid(radius):
            self.__radius = radius
        
        
    def getArea(self):
        '''
         Returns:
            TYPE: float.
            Return the Area of the Circle 
       '''
        import math
        return math.pi * (self.__radius**2)
    
    def getPerimeter(self):
        '''
        Returns:
            TYPE: float.
            returns the Perimeter of the circle
        '''
        import math
        return 2 * math.pi * self.__radius
    
    def setRadius(self,radius:float)->None:
        '''
         Args:
            radius (float): Set the new value for the radius of the circle.

        Returns:
            None:
        '''
        try:
            if self.__isRadiusValid(radius):
                self.__radius = radius
        except (ValueError, TypeError) as e:
            print("Radius is not set to new value since the value supplied is incorrect")
            print(e)
     
    def getRadius(self)->float:
        '''
        Returns:
            float: Retursn the Radius of the Circle.

        '''
        return self.__radius
    
    def __isRadiusValid(cls,radius:float)->bool:
        
        '''Returns true if 
           1. the radius is +ve non-zero value 
           2. the radius is of type float or int
         other wise raises exception'''
        if not isinstance(radius,(float,int)):
            raise TypeError("Radius should be of type float or int")
        if not radius > 0 :
            raise ValueError ("Radius should be  +ve non-zero value")
        return True    
        
def basic_test():
    c1 = Circle()
    print(f"Area of circle with radius {c1.getRadius()} cm"\
          f" is {c1.getArea():.2f} sqcm")
    c1.setRadius(5.5)
    print(f"Area of circle with radius {c1.getRadius()} cm"\
          f" is {c1.getArea():.2f} sqcm")
    print(f"Perimeter of circle with radius {c1.getRadius()} cm"\
              f" is {c1.getPerimeter():.2f} sqcm")
        
    radius = float(input("Please enter the Radius : "))
    c1.setRadius(radius)
    print(f"Area of circle with radius {c1.getRadius()} cm"\
          f" is {c1.getArea():.2f} sqcm")
    print(f"Perimeter of circle with radius {c1.getRadius()} cm"\
              f" is {c1.getPerimeter():.2f} sqcm")
    
        
    radius = float(input("Please enter the Radius : "))
    c2 = Circle(radius)
    print(f"Area of circle with radius {c2.getRadius()} cm"\
          f" is {c2.getArea():.2f} sqcm")
    print(f"Perimeter of circle with radius {c2.getRadius()} cm"\
              f" is {c2.getPerimeter():.2f} sqcm")
        
if __name__ == '__main__':
   basic_test()
   try:
       c1 = Circle(5.0)
       area = c1.getArea()
       perimeter = c1.getPerimeter()
       print(f"Radius = {c1.getRadius()}, Area = {area:.2f}, Perimeter = {perimeter:.2f}")
       c1.setRadius(7.7)
       print(f"Radius = {c1.getRadius()}, Area = {c1.getArea():.2f}," \
             f"Perimeter = {c1.getPerimeter():.2f}")
   except ValueError as e:
       print(e)
   except TypeError as e:
          print(e)
   
   # print(c1.__radius)
   # c1.__doit()
   
       
 