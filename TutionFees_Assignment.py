# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:43:10 2021

@author: Akash
"""


# Suppose that the tuition for a university is Rs 50,000 this year and increases 7% every year.
# In how many years will the tuition have doubled?
# Before you attempt to write a program, first consider how to solve this problem by hand. 
# The tuition for the second year is the tuition for the first year * 1.07.
# The tuition for a future year is the tuition of its preceding year * 1.07. So, 
#the tuition for each year can be computed as follows:
# year = 0 # Year 0
# tuition = 10000
# year += 1 # Year 1
# tuition = tuition * 1.07
# year += 1 # Year 2
# tuition = tuition * 1.07
# year += 1 # Year 3
# tuition = tuition * 1.07
# ...
# write a function that takes the tution fees and rate of increase per year as
# arguments and returns in how many years the fees will be doubled.

def calculate_tution_fees(tution_fees:int, percent_increase_per_year_fees:int) -> int:
    number_of_years = 0
    double_tution_fees = tution_fees * 2
    while tution_fees < double_tution_fees:
        number_of_years += 1
        tution_fees = tution_fees * (1 + percent_increase_per_year_fees/100)
    return number_of_years    
    
if __name__ == "__main__":
    tution_fees                    = 50000
    percent_increase_per_year_fees = 7
    number_of_years = calculate_tution_fees(tution_fees,percent_increase_per_year_fees)
    
    print(f"""\tThe tuition fees {tution_fees} of university this year
and increases by {percent_increase_per_year_fees}% per year will
be doubled in {number_of_years} year""")













