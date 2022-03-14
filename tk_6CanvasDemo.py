# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:36:52 2022

@author: Akash
"""


#You use the Canvas widget for displaying shapes.
#You can use the methods create_rectangle, create_oval, create_arc,
#create_polygon, or create_line to draw a rectangle, oval, arc, 
#polygon, or line on a canvas

from tkinter import Frame
from tkinter import Button
from tkinter import Canvas

class CanvasDemo:
    
    def __init__(self):
        self.__compose_window()
        # Place canvas in the __window
        self.__compose_canvas()
        # Place buttons in self.__frame
        self.__compose_frame()
        self.__window.mainloop() # Create an event loop

    def __compose_window(self):
        self.__window = Tk() # Create a self.__window
        self.__window.title("Canvas Demo") # Set title
        self.__window["bg"] = "yellow"
        self.__window.geometry("330x150")
        
    def __compose_canvas(self):
        self.__canvas = Canvas(self.__window, 
                             width = 200, 
                             height= 100, 
                             bg    = "white")
        self.__canvas.pack()
        
    def __compose_frame(self):
        self.__frame = Frame(self.__window)
        self.__frame["bg"] = "yellow"
        self.__compose_widgets_on_frame1()
        self.__frame.pack()
        
    
    def __compose_widgets_on_frame1(self):
        self.__btRectangle = Button(self.__frame, 
                             text    = "Rectangle",
                             command = self.__displayRect)
        
        self.__btOval      = Button(self.__frame, 
                             text    = "Oval",
                             command = self.__displayOval)
        
        self.__btArc       = Button(self.__frame, 
                             text    = "Arc",
                             command = self.__displayArc)
        
        self.__btPolygon   = Button(self.__frame, 
                             text    = "Polygon",
                             command = self.__displayPolygon)
        
        self.__btLine      = Button(self.__frame, 
                             text    = "Line",
                             command = self.__displayLine)
        
        self.__btString   = Button(self.__frame, 
                             text    = "String",
                             command = self.__displayString)
        
        self.__btClear     = Button(self.__frame, 
                             text    = "Clear",
                             command = self.__clearCanvas)
        
        self.__place_widgets_on_frame1()
        
    
    def __place_widgets_on_frame1(self):
        #       The grid manager places the buttons in one row in a self.__frame
        self.__btRectangle.grid(row = 1, column = 1, padx = 2, pady = 2)
        self.__btOval.grid(     row = 1, column = 2, padx = 2, pady = 2)
        self.__btArc.grid(      row = 1, column = 3, padx = 2, pady = 2)
        self.__btPolygon.grid(  row = 1, column = 4, padx = 2, pady = 2)
        self.__btLine.grid(     row = 1, column = 5, padx = 2, pady = 2)
        self.__btString.grid(   row = 1, column = 6, padx = 2, pady = 2)
        self.__btClear.grid(     row = 1, column = 7, padx = 2, pady = 2)
                
    # display a rectangle
    def __displayRect(self):
        self.__canvas.create_rectangle(10, 10, 
                                     190, 90, 
                                     tags = "rect")
        
    # display an oval
    def __displayOval(self):
        self.__canvas.create_oval(10, 10, 
                                190, 90, 
                                fill = "red",
                                tags = "oval")
    
    # display an arc
    # The width argument can be used to specify the pen size 
    # in pixels for drawing the shapes    
    def __displayArc(self):
        self.__canvas.create_arc(10, 10, 
                               190, 90, 
                               start = 270,   
                               extent= 90, 
                               width = 5, 
                               fill  = "red", 
                               tags  = "arc")
    
    # __display a polygon
    def __displayPolygon(self):
        self.__canvas.create_polygon(10, 10, 
                                   100, 20, 
                                   190, 90, 
                                   50, 80, 
                                   5,40, 
                                   fill = "green",  
                                   tags = "poly")
    
    # __display a line
    # The arrow argument can be used with create_line to draw a 
    # line with an arrowhead. 
    # The arrowhead can appear at the start, end, or both ends of 
    # the line with the argument value first, end, or both.
    def __displayLine(self):
        self.__canvas.create_line(10, 10, 
                                190, 90, 
                                width = 15,
                                fill = "red", 
                                tags = "line")
        # The activefill argument makes the shape change color 
        # when you move the mouse over
        self.__canvas.create_line(10, 90, 
                                190, 10, 
                                width      = 9, 
                                arrow      = "last", # first last both
                                fill       = "blue", 
                                activefill = "cyan", 
                                tags       = "line")
#    activefill = "#ff0000"


    # __display a string
    # create_text method is used to draw a text string
    def __displayString(self):
        self.__canvas.create_text(100, 10, 
                                text = "Hi I am a String", 
                                font = "Times 20 bold underline", 
                                activefill = "green",
                                tags = "string")
    
    # Clear drawings
    # delete method for clearing the drawing from the canvas
    # methods use the tags argument to identify the drawing   
    def __clearCanvas(self):
        self.__canvas.delete("rect", "oval", "arc", "poly", "line", "string")
        
if __name__ == '__main__':  
    CanvasDemo() # Create GUI 
