# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:09:06 2021

@author: Akash
"""

# using with command
# note the difference between readline and read
# note we are not closing the file explicitly

def with_stmt_demo1():
    with open('FH_8_with.txt') as my_file:
        #attempts to read the entire file at one go
        print(my_file.read())   #discards newline
  
def with_stmt_demo2():
    with open('FH_8_with.txt') as my_file:
        #readlines returns list of lines from the file
        print(my_file.readlines())   #retains newline

def with_stmt_demo3():
    with open('FH_8_with.txt') as my_file:
        lines_list = my_file.readlines()
        print("type of lines_list :", type(lines_list))
        print("File Contents in list  are:\n",lines_list)
        print("The first two lines from file are:\n",lines_list[1],lines_list[1])
        print("All the lines from file are as follows :")
        for line in lines_list:
            print(f"\t{line}",end='')
        

def with_stmt_demo4():
    #using for
    with open('FH_8_with.txt') as my_file:
        for line in my_file:
            print(f"\t{line.upper()}",end= '')  

        
if __name__ == '__main__':
    # with_stmt_demo1();
    # with_stmt_demo2();
    # with_stmt_demo3();
    with_stmt_demo4();
    
    
    
    
    
