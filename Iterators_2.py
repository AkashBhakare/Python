# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:10:31 2021

@author: Akash
"""

# The Iterators  is an abstraction, which enables the progrrammer
# to access all the elements of a container
# Iterators  ara a fundamental concept of python.

players = ["Sachin","Vinod","Javagal","Anil","Saurav"]
print("Traversing the itreable using implicit iterator")
for player in players:
    print("player :",player)
    
# The function "iter" is called on the iterable.
# The return value of iter is an iterable. we can iterate Over
# this iterable with the next function until the iterable is
# exhausted and returns a StopIteration Exception

print("Traversing the iterable using iterator exlicitely")
player_iterator = iter(players)
print("player Iterator ",player_iterator)

print("player :",next(player_iterator))
print("player :",next(player_iterator))
print("player :",next(player_iterator))
print("player :",next(player_iterator))
print("player :",next(player_iterator))
#print("player :",next(player_iterator)) #StopIteration Exception

# you can also traverse the python iterator
# using the __next__() method
print("Traversing the iterable using iterator explicitely")
player_iterator = iter(players)

print("player :",player_iterator.__next__())
print("player :",player_iterator.__next__())
print("player :",player_iterator.__next__())

alist = [1,2,3,4,5,6,7,8]
# list_iterator
list_iter = iter(alist)
print(f"iterator type : {type(list_iter)}")
print(list_iter.__next__())

d= {"a":1,"b":2,"c":3}
# dict_keyiterator
dict_iterator = iter(d)
print(f"Iterator type : {type(dict_iterator)}")
print(list_iter.__next__())


dict_iterator = iter(d)
print(d[dict_iterator.__next__()])

#dict_valueiterator
dictVal_Iter = iter(d.values())
print(f"Iterator type : {type(dictVal_Iter)}")
print(dictVal_Iter.__next__())

s = {1,3,6,8,9}
set_iter = iter(s)
print(f"Iterator type :{type(set_iter)}")



































