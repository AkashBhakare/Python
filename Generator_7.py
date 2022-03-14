# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:38:54 2021

@author: Akash
"""


def simpleGen():
    counter = 1
    while True:
        data = yield counter
        print("data sent :", data)
        counter = counter + 1


def grep(pattern):
    print(f"Looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(f"found '{pattern}' in {line}")
        else:
            print(f"not found '{pattern}' in {line}")

if __name__ == '__main__':
    g = grep("python")  # passing value while creating generator
    next(g)
    g.send("'Yeah, but no, but yeah, but no'")
    g.send("\'Trying to understand send\'")
    g.send("'python generators rock!'")
