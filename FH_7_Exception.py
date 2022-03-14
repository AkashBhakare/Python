# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 07:57:02 2021

@author: Akash
"""

#demo of try and except in file handling
#program to read specified line number from a file
#demo text file : try.txt

import sys

def write_file(filename):
    import os.path
    import sys
    file_path = os.path.realpath(filename)
    dir_path = os.path.dirname(file_path)
    if(os.path.exists(dir_path)):
        file_obj = open(filename,"w")
        file_obj.write("FirstLine")
        file_obj.close()
    else:
        print("file path is incorrect !",file=sys.stderr)

def file_exception_demo():
    file_str = input("Enter the File name:")
    isFileOpenSuccess = False
    try:
        input_file = open(file_str, mode="r") # potential user error
        isFileOpenSuccess = True
        find_line_int = int(input("Which line (integer):"))# potential user error
        lines = input_file.readlines()
        line_str = lines[find_line_int] # potential user error
        print(f"Line {find_line_int} of file {file_str} is :{line_str}")
    except FileNotFoundError:
        print(f"The file {file_str} doesn't exist!!",file=sys.stderr)
    except IOError:
        print(f"The file {file_str} doesn't exist.",file=sys.stderr)
    except ValueError:
        print("Line  Number isn't a legal line number in digits.",file=sys.stderr)
    except IndexError:
        # get here if line sought doesn't exist
        print(f"Line {find_line_int} of file {file_str} not found",file=sys.stderr)
    finally:
        if( isFileOpenSuccess == True):
            input_file.close()
        print("End of the program")
            
    

if __name__ =='__main__':
    # filename = input('enter the file name to create :')
    # data.txt
    # e:\temp\data.txt
    # z:\folder\data.txt
    # write_file(filename)
    file_exception_demo()
   