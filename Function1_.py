# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:15:32 2021

@author: Akash
"""

# Called for its side effect
def sayHello():
    print("Hello")
    
sayHello()

# specifying that below function returns None
def sayHello()->None:
    print("Hello Good Morning")
    return
    
t = sayHello()    
print("t : ",t,"type(t) : ",type(t))


def greets(name):
    print(f"Hello {name}, Good Morning".format(name))
    print("We missed you !")
    
greets("Rushi")    


# Called for its return value
def addIt(number1,number2)->float:
    result = number1 + number2
    return result

res = addIt(6,6.1)
print("res : ",res,"type(res)",type(res))



# Called for both its side effect and return value
def multiplyBy(number)->int:
    counter = 2
    print(f"{number} * {counter} = {number * counter}".format(number,counter))
    return number * counter

res = multiplyBy(4)
print("res : ",res, "type(res) : ",type(res))