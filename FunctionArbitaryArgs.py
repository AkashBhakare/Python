# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:37:24 2021

@author: Akash
"""

# Function Arbitrary Arguments
#This Can add only two Integers
def add(n1:int, n2:int)->int:
    result = n1 + n2
    return result

#Can greet only one oerson
def greet(name:str)->None:
    print(f"Hello {name}! How are you?")
    
# *args allow us to pass the variable number of
# non keyword arguments to function

def greet(*names):
    '''Greets number of people'''
    #names is tuple with arguments
    print(type(names))
    print(names)
    for name in names:
        print(f"Hello {name}, How are you?")
  
# *names is reoresenting the arbitary args
#msg is required positional args
def send(msg, *names):
    for name in names:
        print(f'Hello {name},{msg}')
        
        
# *names is representing the arbitary args
# msg is required positional arge
def send(msg, *names):
    for name in names:
        print(f'Hello {name},{msg}')
        
def addNumber(*numbers):
    result = 0
    for value in numbers:
        result = result + value
    return result

def addValues(*numbers):
    '''Function adding arbitary number of integers'''
    return sum(numbers)


#     '''Fun
#     return sum(numbers)
# def add1(count,*args)
#     total = 0
#     for element in args[:count]:
#         total += element
#     return total'''
  
      
def adder1(count, *args):
    total = 0
    for element in args[:count]:
        total += element
    return total

def adder2(*args):
    total = 0
    for element in args:
        total += element
    return total  
#*names is representing the arbitary args
# msg is required positional args
def send(msg:str,*names):
    for name in names:
        print(f"'{msg}' sent to {name}")
        
if __name__ == '__main__':
    greet("Sonia")
    greet("Monica","Sonia","Sahil","Leela")
    print(addNumbers(1,2,3,4,8,9))      
    print(addValues(1,2,3,4,5,78,9))        

    nbr_tup = (1,2,5,6,8)
    print("Sum :",adder1(3,    *nbr_tup))
    print("Sum :",adder1(len(nbr_tup),*nbr_tup))
    print("Sum :",adder1(5,  10,20,30,40,50,60))  
    
    nbr_list = [10,20,30,40,50,60,70]
    print("Sum :",adder1(5,    *nbr_list))
    print("Sum :",adder1(10,    *nbr_list))
    print("Sum :",adder1(100,    *nbr_list))  
    

    #Pass the contents of the iterable
    print("Sum :",adder2(*nbr_tup))
    nbr_tup = (1,3,5,8,1,1,1)
    print("Sum :",adder2(*nbr_tup))
    nbr_list = [10,20,30,40,50,60,70]
    print("Sum :",adder2(*nbr_list))
    print("Sum :",adder2(1.1, 2.2, 3.3, 4.4, 5.5))
    
    evenNumberList = [2,4,6,8]
    # Pass the contents of thr iterable
    print("Sum :",adder2(evenNumberList))
    
    # Pass the iterable itself
    print("Sum :",adder2(evenNumberList))
        
        
        
        
        
        
        
        
        
        
        
        
        


