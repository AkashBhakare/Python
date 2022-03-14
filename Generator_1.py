# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:48:03 2021

@author: Akash
"""

# regular Function
def bar():
    print("Inside a bar")
    counter = 1
    print("Counter = ", counter)
    counter = counter + 1
    print("Counter = ", counter)
    counter = counter + 1
    return counter 

#Simplest generator function
#Rembers the place from where it yielded last

def foo():
    print("Fun started to execute")
    yield 1
    print("Yielding next char value")
    yield 'A'
    print("Yielding float value")
    yield 12.4
    print("Yielding next value")
    yield 'last'
    
#Generator function remember the state of local variables
def baz():
    print("Inside a baz")
    counter = 1
    print("Counter = ", counter)
    counter = counter + 1
    print("Counter = ", counter)
    counter = counter + 1
    return counter 

if __name__ == '__main__':
    x = bar()
    print(f" x = {x}" )
    y = bar()
    print(f" y = {y}" )
    
    x = foo() #return the generator object, doesnt  call foo
    print(x)
    
    y = next(x) #yield 1
    print(f" y = {y}" )

    y = next(x) #yield A
    print(f" y = {y}" )
  
    y = next(x) #yield 12.4
    print(f" y = {y}" )

    y = next(x) #yield last
    print(f" y = {y}" )
    
    y = next(x) #fails stopiteration
    print(f" y = {y}" )


    y = foo()
    print(y)
    print(next(y)) #yields 1
    
    
    g1 = foo()
    g2 = foo()
    
    y = next(g1) 
    print(f" y = {y}" )
    
    y = next(g2) 
    print(f" y = {y}" )
    
    g3 = baz()
    
    y = next(g1) 
    print(f" y = {y}" )
    
    y = next(g3) 
    print(f" y = {y}" )
    
    y = next(g3) 
    print(f" y = {y}" )
    
    y = next(g3) 
    print(f" y = {y}" )















