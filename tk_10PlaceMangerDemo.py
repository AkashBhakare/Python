# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:10:00 2022

@author: Akash
"""


#The place manager places widgets in absolute positions
#The place manager is not compatible with all computers
#you should generally avoid using the place manager
from tkinter import Label # Import tkinter
from tkinter import Tk
    
class PlaceManagerDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Place Manager Demo") # Set title
        
        Label(window, 
              text = "Blue",    
              fg   = 'white', 
              bg="blue").place(x = 20, y = 20)
        
        Label(window, 
              text = "Red",     
              fg   = 'white', 
              bg   = "red").place(x = 150, y = 50)
        
        Label(window, 
              text = "Green",   
              fg   = 'white', 
              bg   = "green").place(x = 80, y = 80)
        
        window.mainloop() # Create an event loop

PlaceManagerDemo() # Create GUI 