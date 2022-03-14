# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:28:43 2021

@author: Akash
"""

# Drawing Preset Figures

import turtle
import time

# Change the Screen Title
turtle.title("My Turtle Program")
# time.sleep(5)

# Return the TurtleScreen object the turtle is drawing on. 
# TurtleScreen methods can then be called for that object.
screen = turtle.getscreen()

# Kind of RawTurtle, has the same interface but draws on a default Screen 
my_turtle = turtle.Turtle()

# Set the turtle’s speed to an integer value in the range 0..10. 
# If no argument is given, return current speed.
my_turtle.speed("slowest")

# turtle.circle(radius, extent=None, steps=None)
# Draw a circle with given radius. 
my_turtle.circle(60)

time.sleep(2)

# Delete the turtle's drawings from the screen.
my_turtle.clear()

my_turtle.circle(120, 90)  # draw a semicircle
time.sleep(3)
my_turtle.reset()

my_turtle.circle(120, 180)  # draw a semicircle
time.sleep(3)
my_turtle.reset()

my_turtle.circle(120, 270)  # draw a semicircle
time.sleep(3)
my_turtle.reset()

my_turtle.circle(120, 360)  # draw a semicircle
time.sleep(3)
my_turtle.reset()


my_turtle.dot(50)

time.sleep(2)
# my_turtle.clear()

screen.bgcolor("green")

time.sleep(2)