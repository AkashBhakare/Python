# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:36:53 2021

@author: Akash
"""

  # A pangram is a sentence that contains all the letters of
  # the English alphabet at least once, for example. 
  # The quick brown fox jumps over the lazy dog.
  # Your task here is to write a function to check a sentence 
  # to see if it is a pangram or not.
  
  
def ispanagram(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    
    for alpha in alphabets:
        if alpha not in string:
            return False
    return True

if __name__ == '__main__':
    string = "The quick brown fox jumps over the lazy dog"
    if(ispanagram(string) == True):
        print("The string is panagram")
    else:
        print("The string is not panagram")