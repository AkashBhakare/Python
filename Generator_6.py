# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:37:25 2021

@author: Akash
"""


def simpleGen():
    counter = 1
    while True:
        data = yield counter
        print("data sent :", data)
        counter = counter + 1
              
g = simpleGen()
print(next(g))
print(next(g))
print(g.send("Hi"))
print(g.send("Bye"))
print(g.send("Yeah"))
