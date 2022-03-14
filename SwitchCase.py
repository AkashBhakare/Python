# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:58:56 2021

@author: Akash
"""

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something is wrong with internet"

def gm():
            return "good morning"

if __name__=="__main__":
            gm()
            print("HTTP Error Code : 400 ==> ",http_error(400))
            print("HTTP Error COde : 404 ==> ",http_error(404))
            print("HTTP Error COde : 418 ==> ",http_error(418))
            print("HTTP Error COde : 500 ==> ",http_error(500))
