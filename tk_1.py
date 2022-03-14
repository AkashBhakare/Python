# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:53:33 2022

@author: Akash
"""

import tkinter as tk

# Create tk window
root_window = tk.Tk()

root_window.iconbitmap('image/pen.ico')
# tk.Label() which will hold our "Hello World" text. 
# The first argument to a Tk widget is the parent in which it will be placed.
label = tk.Label(root_window, 
                 text       = "Hello ! Welcome to Impetus", 
                 padx       = 20,  #internal padding x
                 pady       = 20,  #internal padding y
                 foreground = "red", 
                 background = "#3399FF")

# place the label into the root_window
label.pack()

# root_window.mainloop() is responsible for showing the window.
root_window.mainloop()
