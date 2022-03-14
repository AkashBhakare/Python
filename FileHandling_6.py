# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 08:11:12 2021

@author: Akash
"""

#demo of try and except in file handling
#program to read specified line number from a file
#demo text file : try.txt


def write_file(filename):
    import os.path
    import sys
    file_path = os.path.realpath(filename)
    dir_path = os.path.dirname(file_path)
    if(os.path.exists(dir_path)):
        file_obj = open(filename,"w")
        file_obj.write("FisrtLine")
        file_obj.close()
    else:
        print("file path is incorrect !",file=sys.stderr)

def file_exception_demo():
    file_str = input("Enter the File name:")
    isFileOpenSuccess = False
    try:
        input_file = open(file_str,mode="r") # potential user error
        isFileOpenSuccess = True
        find_line_str = input("Which line (integer):")
        find_line_int = int(find_line_str) # potential user error
        line_count_int = 1
        for line_str in input_file:
            if line_count_int == find_line_int:
                print("Line {} of file {} is :{}".
                      format(find_line_int, file_str,line_str))
                break
            line_count_int += 1
        else:
              # get here if line sought doesn't exist
            print(f"Line {find_line_int} of file {file_str} not found")
        
    except FileNotFoundError:
        print(f"The file {file_str} doesn't exist!!")
    except IOError:
        print(f"The file {file_str} doesn't exist.")
    except ValueError:
        print(f"Line  {find_line_str} isn't a legal line number in digits.")
        
    finally:
        if( isFileOpenSuccess == True):
            input_file.close()
            
    print("End of the program")

if __name__ =='__main__':
    filename = input('enter the file name to create :')
    data.txt
    e:\temp\data.txt
    z:\folder\data.txt
    write_file(filename)
    file_exception_demo()
   