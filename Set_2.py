# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:34:47 2021

@author: Akash
"""

# Frozenset 
# Creating frozenset using list
mylist = [2, 3, 5, 7, 2]
print("My list : ",mylist)
print(mylist)

small_primes = frozenset(mylist)
print("Small primes :", small_primes)

bigger_primes = frozenset(mylist)
print("Bigger primes : ",bigger_primes)

#frozen set are immutable
small_primes.add(11)    #Error
small_primes.remove(2)  #Error

even_set = {2,6,8,12}
prime_set ={19,29,93}

primes = frozenset(prime_set)

print(primes)
#cannot create a set of mutable elements
number_set = {even_set, prime_set}
number_set = {{1, 2, 3}, {5, 7, 5}}
number_set = {[1, 2, 3],[4, 56, 7]}

# We can creates set of Frozen set:
    #Frozenset are immutable
    #Frozenset are hashable
number_set = {bigger_primes, small_primes}
print(number_set)

#ramdom dictionary
person = {"name":"jay", "age":23, "gender":"male"}
print(type(person))

# creating frozenset using dictionary
fset = frozenset(person)
print('The frozen is:\n', fset)

print("small prime : ", small_primes)
print("Bigger primes : ",bigger_primes)
print(small_primes.intersection(bigger_primes))
print(small_primes & bigger_primes)

print("Union : ",small_primes.union(bigger_primes))

oddNums = set([1,3,5,7,9])
print("Union : ",small_primes.union(oddNums))
















