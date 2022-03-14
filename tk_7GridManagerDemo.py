# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:39:04 2022

@author: Akash
"""

import tkinter as tk  # Import tkinter

from tkinter import Tk  # Import tkinter
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Message

# Tkinter supports three geometry managers:
# the grid manager, the pack manager, and the place manager.
# The grid manager places widgets into the cells of an invisible
# grid in a container. You can place a widget in a specified row
# and column. You can also use the rowspan and columnspan parameters
# to place a widget in multiple rows and columns


class GridManagerDemo:
    def __init__(self):
        self.__window = Tk()  # Create a self.__window
        self.__compose_window()
        
        message = Message(self.__window, 
                          text="This Message widget occupies three rows and two columns skk kasdbf klsbdafkijb dsfksb dfksb df dlgfkn ldsgn laksfn lasfjn lasdnfl; sfn ;lsnflasdnf erg er er ert erte rter taert sdfg dsfg sdfg sdfg sdfg sdfg dsfg dsfg dsf g")
    #    use the rowspan and columnspan parameters to place a widget 
    #    in multiple rows and columns.
    #    The Message widget is placed in row 1 and column 1 and it
    #    expands to three rows and two columns
        message.grid(row = 1, column = 1, rowspan = 5, columnspan = 2)
        
        Label(self.__window, 
              text = "First Name:").grid(row = 1, column = 3)
        
    #    The padx and pady options pad the optional horizontal 
    #    and vertical space in a cell
    #    The ipadx and ipady options to pad the optional horizontal
    #    and vertical space inside the widget borders.
        Entry(self.__window).grid(row  = 1, column = 4, 
                           padx = 5, pady   = 5)
        
        Label(self.__window, text = "Last Name:").grid(row = 2, column = 3)
        
        Entry(self.__window).grid(row = 2, column = 4)
        
    #   Button uses the sticky = E option to stick to the east in 
    #   the cell so that it is right aligned with the Entry widgets 
    #   in the same column  
    #   The sticky option can be any combination of the named 
    #   constants S, N, E, and W, or NW, NE, SW, and SE
    #   The sticky option defines how to expand the widget if 
    #   the resulting cell is larger than the widget itself.
    #   The padx and pady options pad the optional horizontal and 
    #   vertical space in a cell
       
        Button(self.__window,
               text = "Get Name").grid(row  = 3, column = 3, 
                                       padx = 0, pady   = 0,
                                       rowspan = 3,columnspan = 2,
                                       sticky = (tk.N,tk.E))
        
        self.__window.mainloop() # Create an event loop
        
    def __compose_window(self):
        self.__window.title("Grid Manager Demo")  # Set title
        self.__window["bg"] = 'cyan'

if __name__ == '__main__':
    GridManagerDemo() # Create GUI     