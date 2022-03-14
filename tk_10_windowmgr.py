# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:59:06 2022

@author: Akash
"""

#the window manager
#in tk, there is a utility command, wm, for interacting with the window manager. 
#options to the wm command allow you to control things like
# titles, placement, icon bitmaps, and the like. in tkinter, 
# these commands have been implemented as methods on the wm class. toplevel
# widgets are subclassed from the wm class, and so can call the wm methods directly.

 #to get at the toplevel window that contains a given widget, you can often
 #just refer to the widget’s master. of course if the widget has been packed inside of a 
 #frame, the master won’t represent a toplevel window. to get at the toplevel window that contains
 #an arbitrary widget, you can call the _root() method. this method begins with an underscore to 
 #denote the fact that this function is part of the implementation, and not an interface to tk
 #functionality.

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()