# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 09:54:27 2021

@author: Akash
"""


import sys

# Private data Member

class Person:
   # Private method 
   def __isNameOnlySpaces(self,name)->bool:
       '''return True if the name is valid otherwise returns False'''
       return name.isspace()
            
       
   def __init__(self, name:str , alias:str ):
      if (not isinstance(name, str)):
          raise TypeError("Error! : Name has to be a String")
      
      if (not isinstance(alias, str)):
          raise TypeError("Error! :  Alias has to be a String")    
      
      if self.__isNameOnlySpaces(name): ##Accessing Private method within class
         raise ValueError("Error! : Value supplied for name is invalid ")
          
      if self.__isNameOnlySpaces(alias): ##Accessing Private method within class    
        raise ValueError("Error! : Value supplied for alias is invalid ")
      
      self.__name  = name
      self.__alias = alias
      
#end of Init
    
   def getAlias(self):
       return self.__alias
   
   def setAlias(self,newAlias:str):
       if (not isinstance(newAlias, str)):
          raise TypeError("Error! :  Alias has to be a String")    
       if self.__isNameOnlySpaces(newAlias): ##Accessing Private method within class    
          raise ValueError("Error! : Value supplied for alias is invalid ")  
       self.__alias = newAlias

   def who(self)->None:
      print(f'name  : {self.__name}')
      print(f'alias : {self.__alias}')
  
if __name__ == '__main__':
    try:
        print("P1")
        p1 = Person("ManvendraSingh","Manu")
        p1.who()
        print("P2")
        # p2 = Person(1212 ," ")
        # p2 = Person("  ",1212)
        # p2 = Person("  ","Babu")
        p2 = Person("Raghavendra Singh","raga")
        p2.who()
        # print(p2.__alias)
        print(p2.getAlias())
        p2.setAlias("Raghu")
        print(p2.getAlias())
        # print(p1.__isNameOnlySpaces("s")) ## Error
    except ValueError as ve:
        print(ve,file=sys.stderr)
    except TypeError as te:
        print(te,file=sys.stderr)
    
    
