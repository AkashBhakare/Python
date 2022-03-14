# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:30:37 2021

@author: Akash
"""


import turtle
import time

screen = turtle.getscreen()
my_turtle = turtle.Turtle()

# change the color of the turtle: this changes the fill color.
# change the color of the pen: this changes the outline or the ink color.

my_turtle.shapesize(3,3,3)

# change the color of the turtle 
# my_turtle.fillcolor("red")
# time.sleep(2)

# change the color of the pen (or the outline)
# my_turtle.pencolor("green")
# my_turtle.pensize(10)
# my_turtle.forward(100)
# time.sleep(3)

# to change the color of both
# fill = yellow
# outline = cyan
# my_turtle.color("cyan", "yellow")
# my_turtle.forward(100)
# time.sleep(3)



# my_turtle.reset()
# my_turtle.speed("slowest")
my_turtle.pensize(5)
my_turtle.pencolor("green")
#return or set the fillcolor.
my_turtle.fillcolor("violet")
my_turtle.fillcolor((187,38,149))
my_turtle.fillcolor('#42ba95')
#called just before drawing a shape to be filled.
my_turtle.begin_fill()
numberofturns = 0
while (numberofturns <= 3):
    my_turtle.forward(100)
    my_turtle.left(90)
    numberofturns = numberofturns + 1
else:
    # fill the shape drawn after the call begin_fill().
    my_turtle.end_fill()


# color(colorstring1, colorstring2), color((r1,g1,b1), (r2,g2,b2))
# equivalent to pencolor(colorstring1) and fillcolor(colorstring2)

# my_turtle.color("cyan", "orange")
# my_turtle.backward(100)
# my_turtle.right(90)
# my_turtle.color("#285078", "#a0c8f0")
# my_turtle.backward(100)

# time.sleep(3)



# my_turtle.goto(200,200)
# my_turtle.home()
# my_turtle.clear()


#changing the turtle shape
my_turtle.shape("turtle")
time.sleep(2)
my_turtle.shape("arrow")
time.sleep(2)
my_turtle.shape("circle")
time.sleep(2)
my_turtle.shape("square")
time.sleep(2)
my_turtle.shape("triangle")
time.sleep(2)
my_turtle.shape("classic")
time.sleep(2)


# Customizing in One Line
my_turtle.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=2)
my_turtle.begin_fill()
my_turtle.circle(90)
my_turtle.end_fill()
time.sleep(5)

