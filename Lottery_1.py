# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:10:56 2021

@author: Akash
"""

# #Case 1:
# lottery = 56
# guess   = 56
# lottery == guess ==> 10,000
# #Case 2:
# lottery = 56
# guess   = 65
# lfd = lottery // 10
# lsd = lottery % 10
# gfd = guess // 10
# gsd = guess % 10
# lfd == gsd and lsd == gfd ==> 3,000
# #Case 3:
# lottery = 56
# guess   = 60
# lfd == gfd or lfd == gsd or lsd == gfd or lsd == gsd ==> 1,000
# #Case 4: 
# Otherwise: ==> Sorry, try again next time.

import random
import sys

from typing import Final

# Generate a lottery
lottery = random.randint(10,99)
print("Generated lottery number ",lottery)

MIN_LIMIT :FINAL = 10
MAX_LIMIT :FINAL = 99

guess = eval(input("Please enter the two digit guess number for your lottery:"))

print("Guess number ",guess)
lfd = lottery // 10
lsd = lottery % 10
gfd = guess // 10
gsd = guess % 10


if (lottery == guess):
    print("Congratulations, you have won Rs 10,000")
elif(lfd == gsd and lsd == gfd):
    print("Congratulations, you have won Rs 3,000")
elif(lfd == gfd or lfd == gsd or lsd == gfd or lsd == gsd):
    print("Congratulations, you have won Rs 1,000")
else:
    print("Sorry, better luck next time")


