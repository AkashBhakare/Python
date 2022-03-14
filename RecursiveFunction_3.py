# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:52:07 2021

@author: Akash
"""


# Recursive function

def isPalindrome(s):
    print(len(s))
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s)-1]:
        return False
    else:
        isPalindrome(s[1:len(s)-1])
        
if __name__ == '__main__':
    num = int(input("Enter a number:"))
    print('Numbers in Ascending order:')
    printAscending(num)
    print('Numbers in Descending order:')
    printDescending(num)
    factorial = getFactorial(num)
    print("Factorial of", num , "=", factorial)
    print("Is aba a palindrome?", isPalindrome("abnna"))
    print("Is ab a palindrome?", isPalindrome("ab"))        