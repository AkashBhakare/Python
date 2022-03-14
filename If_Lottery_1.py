# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:17:45 2021

@author: Akash
"""


# Develop a program to play a lottery. The program randomly generates a
# two-digit number, prompts the user to enter a two-digit number, and determines whether the user wins according to the following rules:
# 1. If the user’s input matches the lottery in the exact order, the award is Rs 10,000.
# 2. If all the digits in the user’s input match all the digits in the lottery number, the award is Rs 3,000.
# 3. If one digit in the user’s input matches a digit in the lottery number, the award is Rs1,000



import random
import sys
from typing import Final

# Generate a lottery
lottery = random.randint(10, 99)

MIN_LIMIT :Final = 10
MAX_LIMIT :Final = 99
# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (two digits): "))

if(guess < MIN_LIMIT or guess > MAX_LIMIT):
    print("You have not entered two digit number",file=sys.stderr)
elif(guess == lottery):
    print("Exact match: you win Rs 10,000")
else:
    guessDigitList   = list(str(guess))
    lotteryDigitList = list(str(lottery))
    guessDigitList.reverse()
    if(guessDigitList == lotteryDigitList):
        print("Match all digits: you win Rs 3,000")
    elif(set(guessDigitList).intersection(set(lotteryDigitList))):
        print("Match one digit: you win Rs 1,000")
    else:
        print("Sorry, no match")
            
print("The Lottery number was : ",lottery)    
  
