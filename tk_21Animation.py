# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:57:39 2022

@author: Akash
"""


# from tkinter import * # Import tkinter
import tkinter as tk

class AnimationDemo:
    def __init__(self):
        self.__window = tk.Tk() # Create a window
        self.__window.title("Animation Demo") # Set a title
        
        self.__width = 250 # Width of the canvas
        self.__canvas = tk.Canvas(self.__window, 
                                  bg = "yellow",
                                  width  = 250, 
                                  height = 150)
        self.__canvas.pack()                                             
        
        x = 0 # Starting x position
        self.__canvas.create_text(x, 30,
                                  text = "Message moving?", 
                                  tags = "text")
        
        self.__canvas.create_oval(x, 100,
                                  x+20,120,
                                  fill = "red",
                                  tags = "oval")
        dx = 3
        while True:
            # move(tagOrId, xAmount, yAmount)
            self.__canvas.move("text", dx, 0) # Move text dx unit
            self.__canvas.move("oval", dx, 0) # Move text dx unit
            # puts the program to sleep for 100 milliseconds
            self.__canvas.after(50) 
            # redisplays the canvas
            self.__canvas.update() # Update canvas
            
            if x < self.__width+30:
                x += dx  # Get the current position for string
            else:
                x = 0 # Reset string position to the beginning
                self.__canvas.delete("text") 
                self.__canvas.delete("oval") 
                # Redraw text at the beginning
                self.__canvas.create_text(x, 30, 
                                   text = "Message moving?",
                                   tags = "text")
                self.__canvas.create_oval(x, 100,
                                  x+20,120,
                                  fill = "red",
                                  tags = "oval")
                
        self.__window.mainloop() # Create an event loop

AnimationDemo() # Create GUI
