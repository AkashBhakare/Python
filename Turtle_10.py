# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:21:59 2021

@author: Akash
"""

import turtle
import time

#change the Screen Title
turtle.title("My Turtule Program")

my_turtle = turtle.Turtle()

colors = ["yello","gold","orange","red","maroon","violet","magenta","purpule"]

my_turtle.speed("normal")
my_turtle.pensize(5)
i = 0
radius = 10
my_turtle.penup()
my_turtle.pendown()
my_turtle.hideturtle()
while radius <= 500:
    my_turtle.pencolor(colors[radius%len(colors)])
    my_turtle.circle(radius)
    radius = radius + 10
    i = i + 1
    my_turtle.up()
    my_turtle.sety(-10*i)
while radius >= 10:
    my_turtle.pencolor("White")
    my_turtle.circle(radius)
    rdius = radius - 10
    i = i - 1
    my_turtle.up()
    my_turtle.sety(-10*i)
    my_turtle.down()
time.sleep(55)
    