# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:24:02 2021

@author: Akash
"""

import turtle
import time

# Change the Screen Title
turtle.title("My Turtle Program")

my_turtle = turtle.Turtle()

colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

#my_turtle.speed("fastest")
#my_turtle.speed("lowest")
my_turtle.speed("normal")
my_turtle.pensize(5)
i = 0
radius = 10

my_turtle.penup()
my_turtle.setpos(0,-200)
my_turtle.pendown()
while radius <= 250:
    my_turtle.circle(radius)
    my_turtle.pencolor(colors[i% len(colors)])
    radius = radius + 10
    i = i + 1
    
i = 0 
radius = 10
radius = 10
my_turtle.pendown()
my_turtle.setpos(200, - 1)
my_turtle.penup()
while radius >= 250:
    my_turtle.circle(radius)
    my_turtle.pencolor(colors[i% len(colors)])
    radius = radius - 10
    i = i + 1
    
time.sleep(15)
