# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:56:55 2021

@author: Akash
"""



# Write a function translate() that will
# translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".


def translate(string):
    consonants='bcdfghjklmnpqrstvwxyz'
    print("".join(l+'o'+l if l in consonants else l for l in string))

string=input("Enter Any String: ")

translate(string)


