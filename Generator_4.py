# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:35:56 2021

@author: Akash
"""

# A return statement inside of a generator is equivalent to raise StopIteration() 


## Generator without raise StopIteration
def gen1():
    yield 99
    
    
## Generator using raise StopIteration
def gen2():
    yield 99
    raise StopIteration(-11)

## Generator using return
def gen3():
    yield 88
    return(-22)
    
if __name__ == '__main__':
    generator = gen1()
    print(next(generator))
    print(next(generator))
    
    generator = gen2()
    print(next(generator))
    print(next(generator))

    generator = gen3()
    print(next(generator))
    print(next(generator))
