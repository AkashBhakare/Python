# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:26:48 2022

@author: Akash
"""

from tkinter import Label  # Import tkinter
from tkinter import Tk
from tkinter import Button

root_window = Tk()  # Create a root window using class Tk

# Create a label
label = Label(root_window, 
              text="Welcome to Python", 
              fg = "blue",
              bg="yellow")  

# Create a button
button = Button(root_window, 
                text="Click Me", 
                fg = "red",
                bg="#42f593")  # #42f593 "#FFFF33" "#87638e" "#f542d1"

label.pack()  # Display the label in the window

button.pack()  # Display the button in the window

# The statement creates an event loop. The event loop processes 
# events continuously until you close the main window
root_window.mainloop() # Create an event loop