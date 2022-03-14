# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:26:46 2021

@author: Akash
"""

# Drawing a Shape
import turtle
import time

screen = turtle.getscreen()
my_turtle = turtle.Turtle()

# my_turtle.speed(1)
# my_turtle.speed("slowest")

# my_turtle.speed(0)
# my_turtle.speed("fastest")

# my_turtle.speed(6)
my_turtle.speed("normal")

my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)

time.sleep(3)