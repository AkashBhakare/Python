# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:23:00 2021

@author: Akash
"""

def foo()->int:
    name = input("What's your name ?")
    print(f"Welcome {name} inside foo")
    return name

def baz()->int:
    num = 9
    print(f"Number in baz :{num}")
    num += 10
    return num


# Error : num1 is local to baz
# print(f"Number1 in baz :{num}")

# def bar()->none:
#     print(f"number1 in bar :{num}")
#     print(f"welcome {name} inside bar")

 
def f()->None:
    num  = 999
    name = "Hrishi"
    print(f"Welcome {name} your lucky number is {num}")
    return
    

if __name__ == '__main__':
    # foo()
    # foo()
    # #print(f"Trying to access {name} outside foo")
    # data = foo()
    # print(f"Trying to access {data} outside foo")
    
    # data = baz()
    # print(f"Data = {data}")
    # data = baz()
    # print(f"Data = {data}")
    
    # num1 is local to baz
    # print(f"number1 in baz :{num1}")
    
    foo()
    baz()
    f()
    f()