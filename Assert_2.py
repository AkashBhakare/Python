# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:42:49 2021

@author: Akash
"""


import sys
import os

def linux_function():
    '''Use this functionn only on linux platform'''
    assert ('linux' in sys.platform), "This code runs on Linux only."
    print("Calling Linux specific services")
    print(os.system('cat try.txt'))
    
    
def windows_function():
    '''Use this functionn only on Windows 32 platform'''
    assert ('win32' in sys.platform), "This code runs on Windows only."
    print("Calling Winndows specific service")
    print(os.system('type d:\Test.java'))
    
if __name__ == '__main__':
    linux_function()
    windows_function()
    