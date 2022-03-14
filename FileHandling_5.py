# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 08:10:07 2021

@author: Akash
"""

# os — Miscellaneous operating system interfaces
# sys — System-specific parameters and functions

def realpath_demo(file_name):
    ''' os.path — Common pathname manipulations '''
    import os
    # construct a path representing the file in the current directory;
    # It is an abstract path- representing existing or non-exsiting file
    filepath = os.path.realpath(file_name)
    print("Path : ", filepath)
    
    # Return True if path refers to an existing path otherwise returns False
    isFilePresent =  os.path.exists(filepath)
    print("Is File present ? ",isFilePresent)
    
def check_if_file_dir_link(filename):
    import os
    filepath = os.path.realpath(filename)
    
    if(os.path.isfile(filepath)):
        print(f"{filepath} : is representing a file")
    elif (os.path.isdir(filepath)):
        print(f"{filepath} : is representing a directory")
       
    print(f"is {filename} a shortcut : {os.path.islink(filepath)}")
    print(f"is {filename} a shortcut : {os.path.islink(filename)}")

def append_and_seek_demo(fileName):
    import os
 # Open a file 'a' :append + read and write
    file_obj = open(fileName, "a+")
 # Append to end of the file
    # file_obj.write("Python is interesting!\n")
    # os.SEEK_SET : 0
    # os.SEEK_CUR : 1
    # os.SEEK_END : 2
    position = file_obj.tell()
    print ("Current file position : ", position)
    # Reposition the file pointer by 0 bytes from the begining of the file
    file_obj.seek(0,os.SEEK_SET)
    # Check current position
    position = file_obj.tell()
    print ("Current file position : ", position)
    #read 10 character from the begining and repositions the file pointer
    string = file_obj.read(10)
    print ("Read String is : ", string)
    print ("Current file position : ", file_obj.tell())
    string = file_obj.read(10)
    print ("Read String is : ", string)
    print ("Current file position : ", file_obj.tell())
   
    file_obj.seek(0, os.SEEK_CUR)
    # can't do nonzero cur-relative seeks
    # file_obj.seek(10, os.SEEK_CUR)
    print ("Current file position : ", file_obj.tell())
    # file_obj.seek(-15, os.SEEK_CUR)
    
     
    # reposition to end of the file
    # file_obj.seek(10, os.SEEK_END)
    # can't do nonzero end-relative seeks
    # file_obj.seek(-10, os.SEEK_END)
    
    # print ("Current file position : ", file_obj.tell())
    
    # skips the first 22 characters from the begining of the file
    file_obj.seek(22, os.SEEK_SET)
    string = file_obj.readline()
    print("Rest of the data after skipping 20 characters:\n",string)
    file_obj.close()


# Test this function on Command prompt and not in IDE
def file_descriptor_demo(filename):
    import os
 # Open a file 'a' :append + read and write
    file_obj = open(filename, "a+")
    print ("Initial file position : ", file_obj.tell())
    file_desc = file_obj.fileno()
    print(f"File descriptor : {file_desc}")
    
    os.lseek(file_desc, 22, os.SEEK_SET)
    print ("After skipping 22 position : ", file_obj.tell())
    line = file_obj.readline()
    print('Line :',line)
    print ("Position after read: ", file_obj.tell())
    
    # negative seek possible usinf file descriptor
    os.lseek(file_desc, -10, os.SEEK_CUR)
    print ("Position after SEEK_CUR: ", file_obj.tell())
    file_obj.seek(0, os.SEEK_CUR)
    print ("Position after SEEK_CUR: ", file_obj.tell())
    line = file_obj.readline()
    print("Line :",line)
    
    #print last ten charaters of the file
    os.lseek(file_desc, -10, os.SEEK_END)
    print ("Position after SEEK_CUR: ", file_obj.tell())
    line = file_obj.readline()
    print("Last ten characters of the file are :",line)
    
if __name__ == '__main__':
    realpath_demo("tempfile.txt")
    check_if_file_dir_link("tempfile1.txt")
    check_if_file_dir_link("India")
    check_if_file_dir_link("zip.lnk")
    check_if_file_dir_link("India123")
    append_and_seek_demo("destdata.txt")
    file_descriptor_demo("destdata.txt")