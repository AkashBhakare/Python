# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:52:14 2021

@author: Akash
"""

#Define Function

def sayHello():
    pass

#Simple Function without parameters and without return
def sayHello():
    print("Hello! Good Evening!")
    print("How are you")
    
#Simple Function with single parameters and without return
def sayHello(name:str)->None:
    print(f'Hello {name}, Good Evening!')
    print(f'I miss You{name}')
   
    
#Function Call
sayHello("Arjun") #String literal as function argument
n = "Neha"
sayHello(n)       #Variable as function argument

sayHello(3.4)
sayHello(34)

#Simple Function definition with two parameter and without return
def sayHello(name1:str, name2:str)->None:
    print(f'{name1} & {name2} are besties!')
    
#Called for its side-effect
def addIt(param1, param2)->None:
    result = param1 + param2
    print("Addition Result = ", result)

#Called for its return value
def multiplyIt(param1:float, param2:float)->float:
    result = param1 * param2
    return result

#Calling function
#sayHello()
ans = addIt(10,20)
print(ans)
addIt("Hello", "Dear")
addIt(1.2, 7.9)

ans = multiplyIt(2, 5)
print(ans)

print(multiplyIt("@",4))
ans = multiplyIt('$',15)
print(ans)


















