# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:30:36 2021

@author: Akash
"""

import turtle
import time

screen = turtle.getscreen()
my_turtle = turtle.Turtle()


# resizemode("user") is called by a call of shapesize with arguments.
# “auto”: adapts the appearance of the turtle corresponding to the value of pensize.
# “user”: adapts the appearance of the turtle according to the values of stretchfactor and outlinewidth (outline), which are set by shapesize().
# “noresize”: no adaption of the turtle’s appearance takes place.
my_turtle.resizemode("user")

# Changing the Turtle Size
# Set/return turtle's stretchfactors/outline. Set resizemode to "user".
# stretch_wid : positive number 
# stretch_len : positive number 
# outline : positive number
my_turtle.shapesize(1,5,10)
time.sleep(2)
my_turtle.clear()

my_turtle.turtlesize(10,5,1)
time.sleep(2)
my_turtle.clear()

my_turtle.shapesize(1,10,5)
time.sleep(2)
my_turtle.clear()

my_turtle.shapesize(10,1,5)
time.sleep(2)
my_turtle.clear()

my_turtle.shapesize(10,10,15)
time.sleep(2)
my_turtle.clear()



my_turtle.resizemode("noresize")


# Changing the Pen Size
my_turtle.speed(1)
my_turtle.forward(100)
my_turtle.left(90)

my_turtle.pensize(5)
my_turtle.forward(100)
my_turtle.left(90)

my_turtle.pensize(10)
my_turtle.forward(100)
my_turtle.right(90)

my_turtle.pensize(20)
my_turtle.forward(100)
my_turtle.right(90)

my_turtle.pensize(30)
my_turtle.forward(100)
my_turtle.left(90)


# Changing the Turtle and Pen Color


time.sleep(3)