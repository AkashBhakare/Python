# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:34:58 2022

@author: Akash
"""

from tkinter import Tk  # Import tkinter
from tkinter import Frame
from tkinter import Label
from tkinter import Radiobutton
from tkinter import StringVar
from tkinter import Button
from tkinter import Entry
from typing import Final
    
class ChangeLabelDemo:
    DEFAULT_TEXT :Final =  "Programming is fun"
    
    def __init__(self):
        window = Tk() # Create a window 
        window.title("Change Label Demo") # Set a title
        
        # Add a label to frame1
        self.frame1 = Frame(window) # Create and add a frame to window 
        self.__compose_frame1()
        
        # Add a label, an entry, a button, and two radio buttons to frame2
        self.__frame2 = Frame(window) # Create and add a frame to window 
        self.__compose_frame2()
        
        window.mainloop() # Create an event loop

    def __compose_frame1(self):
        self.__lbl = Label(self.frame1, text = self.DEFAULT_TEXT)
        self.__lbl["bg"] = "yellow"
        self.__lbl.pack()
        self.frame1.pack()
        
    def __compose_frame2(self):
        self.__label = Label(self.__frame2,  text = "Enter text: ")
        self.__compose_entry()
        
        self.__btChangeText = Button(self.__frame2, 
                              text = "Change Text",
                              command = self.__processButton)
        self.__compose_radio_btns()
        self.__place_widgets_frame2()
        self.__frame2.pack()
    
    def __compose_entry(self):
        self.__msg = StringVar()
#       A text entry field, also called a text field or a text box.
        self.__entry = Entry(self.__frame2, textvariable = self.__msg) 
        
        self.__msg.set(self.DEFAULT_TEXT)
        
        
    def __compose_radio_btns(self):
        self.__v1 = StringVar()
        self.__rbRed = Radiobutton(self.__frame2, 
                            text     = "Red", 
                            bg       = "red", 
                            variable = self.__v1, 
                            value    = 'R',
                            command  = self.__processRadiobutton) 
        
        self.__rbGreen = Radiobutton(self.__frame2, 
                              text     = "Green", 
                              bg       = "green", 
                              variable = self.__v1, 
                              value    = 'G', 
                              command = self.__processRadiobutton) 
        self.__v1.set('G')   
        
        
    def __place_widgets_frame2(self):
        self.__label.grid(       row = 1, column = 1)
        self.__entry.grid(       row = 1, column = 2)
        self.__btChangeText.grid(row = 1, column = 3)
        self.__rbRed.grid(       row = 1, column = 4)
        self.__rbGreen.grid(     row = 1, column = 5)
        
# When you construct a widget, you can specify its properties 
# such as fg, bg, font,cursor, text, and command in the constructor. 
# Later in the program, you can change the widget’s properties 
# by using the following syntax:
# widgetName["propertyName"] = newPropertyValue
 
    def __processRadiobutton(self):
       
        if self.__v1.get() == 'R':
            self.__lbl["fg"] = "red"
        else:
            self.__lbl["fg"] = "green" 
          
    
    def __processButton(self):
        
        msg =  self.__msg.get().strip() # Current value of Entry
        
        if(len(msg) > 0 ):
            self.__lbl["text"] = msg # New text for the label
        else:
            self.__lbl["text"] = self.DEFAULT_TEXT
            self.__msg.set(self.DEFAULT_TEXT)
    
if __name__ == '__main__':      
    ChangeLabelDemo() # Create GUI 
