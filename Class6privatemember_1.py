# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 09:54:26 2021

@author: Akash
"""


# Private data Member

class Person:
   def __init__(self, name, alias):
      self.name    = name    # public
      self.__alias = alias   # private
     
   def who(self):
      print(f"Name   : {self.name}")
      print(f"Alias  : {self.__alias}")

   def getName(self):
      return self.name
 
   def getNameAlias(self):
       return self.__alias
       
      
#Non Member function
def someOtherFunction(person:Person)->None:
    print("Name : ", person.name)
    # print("Alias : ",person.__alias) #Error
    
#    print("Alias : ",p1._Person__alias) # Way out
    
if __name__ == '__main__':
    
    p1 = Person("Shubhshree","Bobby")
    p1.who()
    print("Name : ",  p1.name)
    # print("Alias : ", p1.__alias) ## Error
    print("Alias : ", p1._Person__alias) ## Way out : Okay
    
    print("Name : ",  p1.getName())
    print("Alias : ", p1.getNameAlias()) ## Error
    
    someOtherFunction(p1)
    p1.name = "!@#$%"
    
    p1 = Person(123 ,"123 ")
    p1 = Person(" ", " ")
 