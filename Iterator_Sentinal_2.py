# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:56:40 2021

@author: Akash
"""

class SentinalRepeater:
    
    def __int__(self, value, sentinal):
        self.value = value
        self.sentinal = sentinal
        self.data = value.split()
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.data == self.data.sentinal:
                raise StopIteration
            return self.data
        
text = "sdf eee ffff ggg"
ref = SentinalRepeater(text,'ffff')
iterator = iter(SentinalRepeater(text,'ffff'))
for word in iterator:
    print(word)
    