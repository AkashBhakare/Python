# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:06:03 2021

@author: Akash
"""

import turtle
turtle.speed(0)

for i in range(40):
    for colours in ["red","magenta","blue","green","orange"]:
        turtle.color(colours)
        turtle.pensize(1)
        turtle.left(19)
        turtle.forward(200)
        turtle.left(90) 
        turtle.forward(200)
        turtle.left(90) 
        turtle.forward(200)
        turtle.left(90) 
        
        