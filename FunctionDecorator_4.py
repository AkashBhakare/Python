# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:13:05 2021

@author: Akash
"""

from datetime import datetime

def only_during_office_hours(func):
    def wrapper():
        if 10 <= datetime.now.hour < 18:
            func()
        else:
            print("It's rest time now")
            pass  #Hush, the neighbors are asleep
        return wrapper  
    
#end of decorator 'only_during_office_hours'


@only_during_office_hours 
def doit():
    print("Okay I will get the work done!")
    
    
#say_whee = only_during_office_hours(say_whee)

def wish_by_time(func):
    
    def greet_with_msg(name):
        name = func(name)
        if datetime.now().hour < 12:
            return f"Good Morning! {name}"
        elif datetime.now().hour < 16:
           return f"Good Afternoon! {name}" 
        else:
           return f"Good Night! {name}"
    return greet_with_msg 
   
#end of decorator wish_by_time

@wish_by_time
def wish(name):
    return name.capitlize()


def greet(*names):
    if len(names) != 0:
        for name in names:
            print(wish(name))
            
greet('Rajeev','ManDAR','SheKAR')
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        