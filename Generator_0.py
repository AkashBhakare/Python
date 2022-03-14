# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:29:11 2021

@author: Akash
"""

def foo():
    print('Cricket')
    print('Kabaddi')
    print('Lingrochya')
    print('Hockey')

  

def sportsGenerator():
    counter = 1
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Cricket")
    print("getting sport : ", counter)
    counter = counter + 1
    yield("FootBall") 
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Hockey")
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Tennis")
    print("getting sport : ", counter)
    counter = counter + 1
    yield("BasketBall") 
    print("getting sport : ", counter)
    counter = counter + 1
    yield("Kabaddi")
    return 'No more sports'
   

if __name__ == '__main__':
    # foo()
    # foo()
    # foo()
     
    ## returns a  iterator, i.e. a generator object
    sport = sportsGenerator() 
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    result = next(sport)
    print(result)
    
    
    ## The iterator can be used by calling the next method.
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    print("Sport : ", next(sport))
    #print("Sport : ",next(sport)) ## StopIteration Exception
    
