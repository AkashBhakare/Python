# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:40:14 2021

@author: Akash
"""

def greet(name):
    while True:
        greetMsg = yield 
        yield greetMsg + " " + name

def genSquaresInf():
    i = 0
    while True:
        i = i + 1
        yield i ** 2 # Resume here later 
    
if __name__ == '__main__':
    g = greet("Akash")
    badWordsList = ["aaa","bbb","ccc"]
    goodWordList = ["Good Morning","Good Evening","ccc","Good Night"]
    
    
    for msg in badWordsList:
        next(g)
        result = g.send(msg)
        print(result)
        
    for msg in goodWordList:
        next(g)
        result = g.send(msg)
        print(result)
    
    for message in goodWordList:
        next(g)
        result = g.send(message)
        if message in badWordsList:
            g.close()
        else:
            print(result)
            
    
        
    # g = genSquaresInf();
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # g.close()
    # print(next(g))       
