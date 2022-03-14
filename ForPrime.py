# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:48:26 2021

@author: Akash
"""
number = int(input("Please enter a integer : "))
factors = 0
iteration_counter = 0

#Alternative 1
# for counter in range(1,(number+1)):
#     iteration_counter = iteration_counter + 1
#     if(number % counter == 0):
#         factors = factors + 1
# #end of for loop
# print(factors)
# if(factors <= 2):
#     print("The number ",number," is prime",sep="")
# else:
#     print("The number ",number," is not prime",sep="")


    
# Alternative : effective only when the number is not prime

# isFactorFound = False
# for counter in range(2, number):
#     iteration_counter = iteration_counter + 1
#     if(number % counter == 0):
#         isFactorFound = True
#         break
# #end of for loop

# if(isFactorFound == True):
#     print("The number ",number," is not prime",sep="")
# else:
#     print("The number ",number," is prime",sep="")
    
# isFactorFound = False
# for counter in range(2, ((number//2)+1)):
#     iteration_counter = iteration_counter + 1
#     if(number % counter == 0):
#         isFactorFound = True
#         break
# # end of for loop

# if(isFactorFound == True):
#     print("The number ",number," is not prime",sep="")
# else:
#     print("The number ",number," is prime",sep="")

import math
isFactorFound = False
for counter in range(2, (int(math.sqrt(number))+1)):
    iteration_counter = iteration_counter + 1
    if(number % counter == 0):
        isFactorFound = True
        break
# end of for loop

if(isFactorFound == True):
    print("The number ",number," is not prime",sep="")
else:
    print("The number ",number," is prime",sep="")
    
    
print("Number of iterations :",iteration_counter)