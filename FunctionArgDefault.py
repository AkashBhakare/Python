# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:32:51 2021

@author: Akash
"""

#We need to call this function with exactly 2 arguments
#both the postional arguments are compulsory

def greetings(name:str, msg:str )->None:
    print(f"Hello {name}, {msg}")
    
greetings("Rushi","Welcome")
greetings("Rushi")
greetings()

#Since the second argument has default value
#We can call this function eith only the name and
#message will get substituted with default argument


def greet(name, msg = "good Morning!"):
    print(f"Hello {name}, {msg}")
    
greet("Rushi","Welcome")
greet("Rushi")
greet()    

#Rule : Positional (required) arguments cannot follow default arguments
#def greet(title = 'Miss',name, msg = "Good Morning!"):
   
def greet(title = 'Miss',name=None, msg = "Good Morning!"):
    print(f"Hello {title}.{name}, {msg}")
    
greet("Mr","Rushi","Welcome")
greet("Mr","Rushi")
greet("Mr")
greet()
greet(name="Jui")

# def greet(title:str = 'Miss',name:str = None, msg:str = "Good Morning!")->None:
#     print(f"Hello {title}.{name}, {msg}")
  

def sendMail(msg, to, cc=None, bcc=None):
    print(f"Sending '{msg}' to {to}")
    if cc is not None:
        print(f"{cc} is informed about the '{msg}' (cc)")
    if bcc is not None:
        print(f"{bcc} is also informed about the '{msg}' {bcc}")
        
   
def bar(one,two=(3,4)):
    print(one,two)
    
def other_dummy():
    mylist = [12,34,5]
    print('I am in!')
    return mylist


def dummy(param=other_dummy()):
    print(param)

import time

def foo():
    now = time.location()
    return time.asctime(now)

def baz(mytime=foo()):
    print(mytime)

import locale
import setlocale
import currency























