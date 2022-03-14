# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:48:51 2021

@author: Akash
"""
# iter Parameters
# iter with sentinal value

text = "Failure will never overtake me if my determination"\
" to succeed is strong enough"

print(text)

print(text.__iter__)

letter_iterator = iter(text)
print(letter_iterator) # Str_iterator

for letter in letter_iterator:
    print(letter)
    
word_list = text.split()
for word in word_list:
    print(word)
    
word_list = text.split()
word_list = (word_list)
for word in word_list:
    print(word)
    

for word in text.split():
    print(word) 
    
word_iterator = iter(text.split())
print(f"Iterator Type {word_iterator}") #list_iterator

for word in word_iterator:
    print(word)
    
word_list = ["happy","fun","game","flower"]


# If the second arguments, sentinel is given then object must be a callable object
word_iterator = iter(word_list.pop,"sad")
#callable_iterator
print(f"Iterator Type {word_iterator}") #list_iterator

for word in word_iterator:
    print(word)
    
    
#iterates till end
myfile = open("dataiter.txt","r")
file_iterator = iter(myfile)
print(f"Iterator Type {file_iterator}")

for word in file_iterator:
    print(word,end="")
    
    
# Using second parameter in iter sentinal
myfile = open("dataiter.txt","r")
fileIterator = iter(myfile.readline,'Forth Line\n')
for word in fileIterator:
    print(word,end="")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    