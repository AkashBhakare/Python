# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:08:11 2021

@author: Akash
"""

num = int(input("Please enter an integer :"))

# Alternative -1
msg = "Even" if (num % 2 == 0) else "Odd"
print(msg)

# Alternative -2
print("Even") if (num % 2  == 0) else("Odd")

#program to compare two integers
a, b = 17, 8
print("a is smaller than b") if(a < b) else print("a id greater than b")

#program to check iff a student cleared the test
score = int(input("Pleasr thr score (out of 100) :"))

#using Tuple
result = ("Fail", "Pass") [score >= 50]
print ("The Result is",result)
#print (result)

#using dictionary
score = 76
print ({True: "Pass", False: "Fail"} [score > 75])
print ({False: "Fail", True: "Pass"} [score > 75])

#using List
score = 75
result = ["Fail", "Pass"][score > 35]
print (result)