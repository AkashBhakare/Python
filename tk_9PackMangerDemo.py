# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:05:41 2022

@author: Akash
"""

import tkinter as tk
from tkinter import Tk  # Import tkinter
from tkinter import Label


# The pack manager can place widgets on top of each other or
# place them side by side. You can also use the fill option to
# make a widget fill its entire container.


class PackManagerDemo:
    
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Pack Manager Demo 1")  # Set title

        # lbl = Label(window, 
        #             text = "Blue", 
        #             bg   = "blue",
        #             fg   = "white")
        
        # lbl.pack(side = tk.RIGHT)

# The fill option uses named constants X, Y, or BOTH to fill horizontally, 
# vertically, or both ways. The expand option tells the pack manager to assign additional space to the widget. 

# If the parent widget is larger than necessary to hold all the 
# packed widgets, any extra space is distributed among the widgets 
# whose expand option is set to a nonzero value
        
        # Label(window, 
        #       text = "Blue",
        #       fg   ='white', 
        #       bg   = "blue").pack(fill = tk.X, expand = 1, side = tk.LEFT)
        
        Label(window, 
              text = "Green1",
              fg   = 'white', 
              bg   = "green").pack(fill = tk.Y, expand = 0,side= tk.LEFT)
        
        # Label(window, 
        #       text = "Blue",
        #       fg   = 'white', 
        #       bg   = "blue").pack(fill = tk.X, expand = 1, side = tk.RIGHT)
     
        
        # Label(window, 
        #       text = "Blue",
        #       fg   = 'white', 
        #       bg   = "blue").pack(fill = tk.X, expand=0, side=tk.LEFT)
        
       
        
#       The side option can be LEFT, RIGHT, TOP, or BOTTOM.
#       By default, it is set to TOP   

        # Label(window, 
        #       text = "Blue", 
        #       fg   = 'white',
        #       bg   = "blue").pack(fill = tk.X, side = tk.TOP)
        
        
        # Label(window, 
        #       text = "Red", 
        #       bg   = "red").pack(fill = tk.BOTH, expand = 1)
        
        Label(window, 
              text = "Green", 
              bg   = "green").pack(fill = tk.Y, expand = 0, side = tk.RIGHT)
        
        window.mainloop() # Create an event loop

if __name__ == '__main__':
    PackManagerDemo() # Create GUI 