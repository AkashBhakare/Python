# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:56:49 2022

@author: Akash
"""


import tkinter as tk


class EnlargeShrinkCircle:
    
    def __init__(self):
        self.__window = tk.Tk() # Create a window
        self.__window.title("Control Circle Demo") # Set a title
        self.__configure_create_canvas()
        self.__radius = 155
        self.__drawCircle()
        self.__window.mainloop() # Create an event loop
        
    def __configure_create_canvas(self):
 
        self.__canvas = tk.Canvas(self.__window, 
                               bg     = "yellow", 
                               width  = 210, 
                               height = 210)
     
        self.__canvas.pack()
           
        # Bind canvas with mouse events
        self.__canvas.bind("<Button-1>", self.__increaseCircle)
        self.__canvas.bind("<Button-3>", self.__decreaseCircle)
        
    def __increaseCircle(self, event):
        if self.__radius < 205:
            self.__radius += 2
            self.__drawCircle()
        
    def __decreaseCircle(self, event):
        
        if self.__radius > 2:
            self.__radius -= 2
            self.__drawCircle()
            
    
    def __drawCircle(self):
        self.__canvas.delete("oval")
        self.__canvas.create_oval(
            int(self.__canvas["width"])  - self.__radius, # x1  top left
            int(self.__canvas["height"]) - self.__radius, # y1  top left
            self.__radius, # x2  bottom right
            self.__radius,
            tags = "oval") # y2  bottom right
        

if __name__ == '__main__':
    EnlargeShrinkCircle() # Create GUI