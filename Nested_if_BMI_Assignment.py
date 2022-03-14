# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:39:24 2021

@author: Akash
"""


# Write a program that interprets body mass index.
# Body mass index (BMI) is a measure of health based on weight.
#  It can be calculated by taking your weight in kilograms and dividing it by the square of your height in meters. 
# The interpretation of BMI for people 16 years and older is as follows:

# BMI 		|	Interpretation
# ____________|___________________
# Below 18.5 	|	Underweight
# 18.5–24.9 	|	Normal
# 25.0–29.9 	|	Overweight
# Above 30.0 	|	Obese

# Write a program that prompts the user to enter a weight in Kilograms and height in inches and then displays the BMI. 
# Note that and one inch is 0.0254 meters.



height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi
bmi = weight/(height**2) 


print("Your BMI is: {0} and you are: ".format(bmi), end='')

#conditions
if ( bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 24.9):
   print("Normal")

elif ( bmi >= 25.0 and bmi < 29.9):
   print("overweight")

elif ( bmi >=30):
   print("Obese")