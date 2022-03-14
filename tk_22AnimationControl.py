# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:00:27 2022

@author: Akash
"""

# from tkinter import * # Import tkinter
import tkinter as tk

class ControlAnimation:
    def __init__(self):
        window = tk.Tk() # Create a window
        window.title("Control Animation Demo") # Set a title
        
        self.width = 250 # Width of the self.canvas
        self.canvas = tk.Canvas(window, bg = "white", 
            width = self.width, height = 50)
        self.canvas.pack()
        
        frame = tk.Frame(window)
        frame.pack()
        btStop = tk.Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = tk.LEFT)
        btResume = tk.tk.Button(frame, text = "Resume", 
            command = self.resume)
        btResume.pack(side = tk.LEFT)
        btFaster = tk.Button(frame, text = "Faster", 
            command = self.faster)
        btFaster.pack(side = tk.LEFT)
        btSlower = tk.Button(frame, text = "Slower", 
            command = self.slower)
        btSlower.pack(side = tk.LEFT)
        
        self.x = 0 # Starting x position
        self.sleepTime = 100 # Set a sleep time 
        self.canvas.create_text(self.x, 30, 
            text = "Message moving?", tags = "text")
        
        self.dx = 3
        self.isStopped = False
        self.animate()
        
        window.mainloop() # Create an event loop
        
    def stop(self): # Stop animation
        self.isStopped = True
    
    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
    
    def faster(self): # Speed up the animation
        if self.sleepTime > 5:
            self.sleepTime -= 20
               
    def slower(self): # Slow down the animation
        self.sleepTime += 20
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0) # Move text 
            self.canvas.after(self.sleepTime) # Sleep 
            self.canvas.update() # Update self.canvas
            if self.x < self.width:
                self.x += self.dx  # Set new position 
            else:
                self.x = 0 # Reset string position to the beginning
                self.canvas.delete("text") 
                # Redraw text at the beginning
                self.canvas.create_text(self.x, 30, 
                    text = "Message moving?", tags = "text")
                
                
                
                #self.__window.mainloop() # Create an event loop

        ControlAnimation() # Create GUI