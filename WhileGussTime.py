# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:52:48 2021

@author: Akash
"""

# While loop with optional else clause
# Guess the number
import random
import time
number = random.randint(0,100)
startTime = time.time() 
running = True  # Note:use of boolean literal

#execute loop repeatedly as long as running is True
while running:
    guess = int(input('Guess the integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False # this causes the while loop to stop
    elif guess < number:    
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The Game is over.')
endTime = time.time()

# Do anything else you want to do here
print('You took',round(endTime-startTime,0),"seconds")

