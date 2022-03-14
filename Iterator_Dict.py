# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:07:19 2021

@author: Akash
"""


statesCapital = {
"Maharashtra"   : "Mumbai",
"Gujarat"       : "Gandhinagar",
"TamilNadu"     : "Chennai",
"Karnstaka"     : "Banglore",
"Kerala"        : "Thiruanantpuram",
"Odisha"        : "Bhuvneshwar"}

for state in statesCapital:
    print(f"The capital of {state}, is {statesCapital.get(state)}")
    
# We can simulate this iteration behavior of the for
# loop in a while loop:
# the iteration runs over the keys of the dictionary
    
stateIterator = iter(statesCapital) #Dict_Keyiterator
print(f"'State Iterator : {type(stateIterator)}")


while True:
    try:
        state = next(stateIterator)
        print(f'{state} : {statesCapital.get(state)}')
    except StopAsyncIteration:
        print("Finished with all the States")
        break
    
print("'Bye Bye")

 











