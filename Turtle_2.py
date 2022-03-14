# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:22:11 2021

@author: Akash
"""


# moving the turtle
#     there are four directions that a turtle can move in:
#         forward
#         backward
#         left
#         right
#     the turtle moves .forward() or .backward() in the direction 
#     that it’s facing.  you can change this direction by turning it 
#     .left() or .right() by a certain degree

import turtle
import time

screen = turtle.getscreen()
my_turtle = turtle.Turtle()

time.sleep(3)

# Move the turtle forward by the specified distance.
my_turtle.forward(100)

# Turn turtle left by angle units.
my_turtle.left(90)

my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)

# time.sleep(3)

# Turn turtle right by angle units.
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
# Move the turtle backward by distance.
my_turtle.backward(100)

# The screen is divided into four quadrants.
# The point where the turtle is initially positioned at the 
# beginning of your program is (0,0). This is called Home
# To move the turtle to any other area on the screen, you use .goto() 

my_turtle.goto(-100,300)
# time.sleep(3)
# Move turtle to the origin - coordinates (0,0).
my_turtle.home()

# You can use the shortened versions of these commands as well:
# my_turtle.rt() instead of my_turtle.right()
# my_turtle.fd() instead of my_turtle.forward()
# my_turtle.lt() instead of my_turtle.left()
# my_turtle.bk() instead of my_turtle.backward()

my_turtle.goto(50,-100)
my_turtle.fd(100)
my_turtle.lt(50)
my_turtle.goto(-150,-100)
my_turtle.bk(100)

time.sleep(5)