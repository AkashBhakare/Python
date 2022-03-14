# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:11:58 2022

@author: Akash
"""

import tkinter as tk
from tkinter import PhotoImage # Import tkinter
from tkinter import Tk # Import tkinter
from tkinter import Frame
from tkinter import Button
from tkinter import Canvas
from tkinter import Checkbutton
from tkinter import Radiobutton
from tkinter import LEFT
from tkinter import Label
from tkinter import messagebox
from tkinter import IntVar

#A photo is an image whose pixels can display any color or be transparent. Image data for a photo image can be obtained from a file or a string. At present, only GIF, PNG and PPM/PGM formats are supported

class ImageDemo:
    def __init__(self):
        self.__createWindowAndFrames()
        self.__createImages()
        self.__placeImageOnLabel()
        self.__placeImageOnCanvas()
        self.__createAndPlaceButtons()
        self.__createAndPlaceCheckBoxWithImage()
        self.__createAndPlaceRadioButtonWithImage()
        self.__window.mainloop() # Create an event loop
        
    def __createWindowAndFrames(self):
        self.__window = Tk() # Create a window
        self.__window.title("Image Demo") # Set title
         # frame1 to contain label and canvas
        self.__frame1 = Frame(self.__window)
        self.__frame2 = Frame(self.__window)
        # self.__frame1["bg"] = "green"
        # self.__frame2["bg"] = "red"
        self.__frame1.pack()
        self.__frame2.pack()
        
    def __createImages(self):
        # Create PhotoImage objects
        self.__inImage    = PhotoImage(file = "image/china.gif")
        self.__chinaImage = PhotoImage(file = "image/china.gif")
        self.__leftImage  = PhotoImage(file = "image/left.gif")
        self.__rightImage = PhotoImage(file = "image/right.gif")
        self.__usImage    = PhotoImage(file = "image/usIcon.gif")
        self.__ukImage    = PhotoImage(file = "image/ukIcon.gif")
        self.__crossImage = PhotoImage(file = "image/x.gif")
        self.__circleImage= PhotoImage(file = "image/o.gif")
    
    def __placeImageOnLabel(self):
        Label(self.__frame1, 
              image = self.__inImage).pack(side = LEFT)
        
    def __placeImageOnCanvas(self):
        self.__canvas = Canvas(self.__frame1)
#       The arguments x and y specify the coordinates of a point  
#       used to position the image on the display
        self.__canvas.create_image(75, 45,image = self.__chinaImage)
        self.__canvas["width"]  = 130
        self.__canvas["height"] = 77
        # self.__canvas["bg"]          = 'yellow'
        self.__canvas.pack(side = LEFT)
    
    def __createAndPlaceButtons(self):
        Button(self.__frame2, 
               image  = self.__leftImage,
               command=self.__leftBtnPressed).pack(side = LEFT)
        
        Button(self.__frame2, 
               image  = self.__rightImage,
               command=self.__rightBtnPressed).pack(side = LEFT) 
        
        
    def __createAndPlaceCheckBoxWithImage(self):
        self.__btn_us_var = tk.IntVar()
        Checkbutton(self.__frame2, 
                    variable = self.__btn_us_var,
                    image   = self.__usImage,
                    command = self.__usBtnClicked).pack(side = LEFT)
        
        self.__btn_uk_var = tk.IntVar()
        Checkbutton(self.__frame2, 
                    variable = self.__btn_uk_var,
                    image   = self.__ukImage,
                    command = self.__ukBtnClicked).pack(side = LEFT)
        
    
    
    def __createAndPlaceRadioButtonWithImage(self):
        self.__choice = IntVar()
        Radiobutton(self.__frame2, 
                    image    = self.__crossImage,
                    variable = self.__choice,
                    command  = self.__radioButtonclicked,
                    value    = 1).pack(side = LEFT)
        
        
        Radiobutton(self.__frame2, 
                    image    = self.__circleImage,
                    variable = self.__choice,
                    command  = self.__radioButtonclicked,
                    value    = 2).pack(side = LEFT)
        
        
    def __leftBtnPressed(self):
        messagebox.showinfo("Button Selection", "You have pressed Rewind button")
    
    
    def __rightBtnPressed(self):
        messagebox.showinfo("Button Selection", "You have pressed Forward button")
    
    
    def __usBtnClicked(self):
        # print(self.__btn_us_var.get())
        if self.__btn_us_var.get() == 1:
            messagebox.showinfo("Check Box Selection", "Welcome to America")
        else:
            messagebox.showinfo("Check Box Selection", "Bye Bye America")
        
        
    def __ukBtnClicked(self):
        if self.__btn_uk_var.get() == 1:
            messagebox.showinfo("Check Box Selection", "Welcome to United Kingdom")
        else:
            messagebox.showinfo("Check Box Selection", "Bye Bye United Kingdom")
        
       
    def __radioButtonclicked(self):
        if self.__choice.get() == 1:
            messagebox.showinfo("Radio Selection", "You have clicked X")
        else:
            messagebox.showinfo("Radio Selection", "You have clicked O")

            
if __name__ == '__main__':
    #print(E)
    ImageDemo() # Create GUI 