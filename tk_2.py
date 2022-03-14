# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:06:55 2022

@author: Akash
"""

## It’s much better to use a class to keep track of all
## individual widgets which may need to reference each other.

import tkinter as tk

# Root class inheriting from Tkinter’s Tk
# This creates a toplevel widget of Tk which usually is the main window of 
# an application. 

class SimpleUI(tk.Tk):  
    
    def __init__(self):
        super().__init__()
        
#       The padx and pady arguments add padding horizontally & vertically.
        self.__label  = tk.Label(self, text="Hello World", padx=5, pady=5)
        
        # Create a button
        self.__button = tk.Button(self, text = "Click Me") 
        
        self.__label.pack()  # Display the label in the window
        self.__button.pack() # Display the button in the window

if __name__ == "__main__":
    root = SimpleUI()
        
    root.mainloop()
    
    