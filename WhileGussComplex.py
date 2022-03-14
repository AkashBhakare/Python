# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:47:14 2021

@author: Akash
"""

## Guess the Number : Only 6 chances
import random

randomNumber = random.randint(1,100)
MAX_CHANCES = 6
chanceCounter = 1
while chanceCounter <= MAX_CHANCES:
    numberGuessed = int(input("Guess the number ? "))
    if numberGuessed == randomNumber:
        print("You Got it Right! You are a winner!!")
        break
    if numberGuessed < randomNumber:
        print("Number is greater than",numberGuessed)
    else:
        print("Number is smaller than",numberGuessed)
    print("You have ",(MAX_CHANCES-chanceCounter),"more attempt left")
    chanceCounter = chanceCounter + 1
else:
    print("You are a Looser!!!!")

