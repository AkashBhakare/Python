# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:30:39 2021

@author: Akash
"""

import turtle
import time

# Change the Screen Title
turtle.title("My Turtle Program")

my_turtle = turtle.Turtle()

# Picking the Pen Up and Down

my_turtle.speed(1)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.penup()
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.pendown()
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.penup()
my_turtle.fd(100)
my_turtle.pendown()

# Resetting the Environment
# The screen will get cleared up, and the turtle’s settings will all be 
# restored to their default parameters
my_turtle.reset()


# Leaving a Stamp
# my_turtle.stamp()

# my_turtle.fd(100)
# my_turtle.stamp()

# my_turtle.fd(100)

# time.sleep(2)