# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:38:08 2022

@author: Akash
"""

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser


#All the dialog boxes are modal windows, which means that 
#the program cannot continue until a dialog box is dismissed.

#The program invokes the showinfo, showwarning, and showerror 
#functions to display an information message, a warning, 
#and an error. 
#These functions are defined in the tkinter.messagebox module

class DialogDemo():
    
    def __init__(self):
        self.__root = tk.Tk()
        tk.Button(self.__root,
                  text = "Info",
                  bg   = '#ffffa6',
                  command = self.__infoDemo).grid(row = 1, column = 1,
                                                  columnspan = 4, 
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.E,tk.W))
        tk.Button(self.__root,
                  text = "Warning",
                  bg   = '#ffffa6',
                  command = self.__warnDemo).grid(row = 2, column = 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))
        tk.Button(self.__root,
                  text = "Error",
                  bg   = '#ffffa6',
                  command = self.__errorDemo).grid(row = 3, column = 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))
        
        tk.Button(self.__root,
                  text = "Yes No Demo",
                  bg   = '#ffffa6',
                  command = self.__yesNoDemo).grid(row = 4, column = 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                           
        tk.Button(self.__root,
                  text = "OK Cancel Demo",
                  bg   = '#ffffa6',
                  command = self.__okCancelDemo).grid(row = 5, column = 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                           
        
        tk.Button(self.__root,
                  text = "Yes No Cancel Demo",
                  bg   = '#ffffa6',
                  command = self.__yesNoCancelDemo).grid(row=6,column= 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                           
        tk.Button(self.__root,
                  text = "Ask Question",
                  bg   = '#ffffa6',
                  command = self.__askQuestionDemo).grid(row=7,column= 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                           
                                                        
        tk.Button(self.__root,
                  text = "Ask Retry",
                  bg   = '#ffffa6',
                  command = self.__askRetryDemo).grid(row=8,column= 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                           
        tk.Button(self.__root,
                  text = "Simple Dialog String",
                  bg   = '#ffffa6',
                  command = self.__askStringDemo).grid(row=9,column= 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                                                                   
        tk.Button(self.__root,
                  text = "Simple Dialog Integer",
                  bg   = '#ffffa6',
                  command = self.__askIntegerDemo).grid(row=10,column= 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                                                                   
        tk.Button(self.__root,
                  text = "Simple Dialog Float",
                  bg   = '#ffffa6',
                  command = self.__askfloatDemo).grid(row=11,column= 1,
                                                  columnspan = 3,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.W,tk.E))                                                                                                                    
        self.colorbtn = tk.Button(self.__root,
                  text = "Choose Color",
                  bg   = '#ffffa6',
                  command = self.__colorChooserDemo)
        self.colorbtn.grid(row=12,column= 1,
                                                  columnspan = 5,
                                                  padx = 10, pady = 5,
                                                  sticky = (tk.E,tk.W))                                                                                                                    
                                                      
        self.__root.mainloop()
         
    def __infoDemo(self):
        tk.messagebox.showinfo("showInfo", "This is an info msg")
        
    def __warnDemo(self):    
        tk.messagebox.showwarning("showWarning", "This is a warning")
    
    def __errorDemo(self):     
        tk.messagebox.showerror("showError", "This is an error")
        
        
# The askyesno function displays the Yes and No buttons in the 
# dialog box. The function returns True if the Yes button is 
# clicked or False if the No button is clicked.
    def __yesNoDemo(self):
        isYes = tkinter.messagebox.askyesno("askYesNo", "Do you want to exit?")
        if(isYes):
            self.__root.quit() #All widgets will be destroyed.
            
# The askokcancel function displays the OK and Cancel buttons 
# in the dialog box. The function returns True if the OK button 
# is clicked or False if the Cancel button is clicked.
    def __okCancelDemo(self):
        isOK = tk.messagebox.askokcancel("askOkCancel", "Shall we quit?")
        if(isOK):
            self.__root.quit()
            
            
#The askyesnocancel function displays the Yes, No, and Cancel 
#buttons in the dialog box. The function returns True if the 
#Yes button is clicked, False if the No button is clicked or 
#None if the Cancel button is clicked.
    def __yesNoCancelDemo(self):
        isYesNoCancel = tk.messagebox.askyesnocancel("askYesNoCancel", "Should we take a break?") 
        if isYesNoCancel == True:
            tk.messagebox.showinfo("Break Msg","Let's take a break..")
        elif isYesNoCancel == False:
            tk.messagebox.showinfo("Break Msg","Let's Not take a break..")
        else:
            tk.messagebox.showinfo("Break Msg","I don't know..")
    
    def __askQuestionDemo(self):    
        # returns 'yes' 'no'
        pastry = tk.messagebox.askquestion(title="Pastry",
                                           message="Do you love Samosa??")
        
        if pastry == 'yes':
            tk.messagebox.showinfo("Pastry","Enjoy Samosa with chutney!")
        else:
            tk.messagebox.showinfo("Pastry","Looks like you are on diet!")
            
    def __askRetryDemo(self):    
        choice = tk.messagebox.askretrycancel(title="Retry ", 
                                              message="Do you want to try again?")
        if choice == True:
            tk.messagebox.showinfo("Retry","Try once again to do it!")
        else:
           tk.messagebox.showinfo("Retry","Let's cancel the attempt")


#The askstring function returns the string entered from the 
#dialog box after the OK button is clicked or None if Cancel button is clicked. 
    def __askStringDemo(self):
        name = tk.simpledialog.askstring("askString", "What's your name ?")
       
        if name is not None :
            name = name.strip()
            if len(name) > 0:
                tk.messagebox.showinfo("Welcome",F"Welcome {name} to Tkinter" )
                return
        tk.messagebox.showinfo("Welcome","Welcome annonymous!")
            
# The askinteger function returns the integer entered 
# from the dialog box after the OK button is clicked or 
# None if the Cancel button is clicked
    def __askIntegerDemo(self):
        lucky = tk.simpledialog.askinteger("Lucky Number", "What's your lucky number?")
        if lucky == None:
            tk.messagebox.showinfo("Lucky","Sorry You don't have a lucky number yet!" )
        else:
             tk.messagebox.showinfo("Lucky",f"Your lucky Number is {lucky} ")
            
#The askfloat function returns the float entered from the 
#dialog box after the OK button is clicked or None if the 
#Cancel button is clicked.
    def __askfloatDemo(self):
        number = tk.simpledialog.askfloat("Real Number", "Enter a real number ")
        if number is not None:
             tk.messagebox.showinfo("Real",F"Your have entered {number} " )
        else:
            tk.messagebox.showinfo("Real","Sorry You have not supplied any number!")

#Create a color choosing dialog. 
# A call to askColor() method will show the window,
# wait for the user to make a selection, 
# and return the selected color (or None) to the caller.
    def __colorChooserDemo(self):
        color = tk.colorchooser.askcolor()
        if None not in [color[0], color[1]]:
            tk.messagebox.showinfo("Color",F"Your have chosed {color[0]} color" )
            self.colorbtn["bg"] = color[1]
        else:
            tk.messagebox.showinfo("Color",f"{color}You haven't made a choice")
            self.colorbtn["bg"] = '#ffffa6'
 
if __name__ == '__main__':
    DialogDemo()