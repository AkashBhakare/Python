# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:25:42 2021

@author: Akash
"""

# glob
#Use Unix shell rules to find filenames matching a pattern.
#It is useful in any situation where a program needs to 
#look for a list of files on the file system with names 
#matching a pattern. 

import glob

# An asterisk (*) matches zero or more characters in a segment of a name.
def listCurrentDirectory():
    # Return a list of paths matching a pathname pattern.
    print("List of elements in the current directory  ")
    for name in glob.glob('*'):
        print(name)
        
    #  In sorted order
    print("List of elements in the current directory in sorted order ")
    fileList = glob.glob('*') #return a list
    sortList = sorted(fileList,key=str.lower,reverse=True)
    
    for fname in sortList:
        print(fname)

# To list files in a subdirectory, the subdirectory must be included in the pattern     
def listFileInSpecifiedDirectory(dir_path:str):
    
    # List only files
    only_files =  glob.glob(dir_path+'\*.*') 
    print("Linting only the file Names")
    for name in sorted(only_files):
        print(name)
    
    print()
    # List Files and directories
    file_and_dir = glob.glob(dir_path+"\*") 
    print("Listing File and directories")
    for name in sorted(file_and_dir):
        print(name)
    
        
# Single Character Wildcard (?)
# It matches any single character in that position in the name.
def listSpecificFiles():
    #List filename the begin with FH_ and is followed by single character
    # for name in sorted(glob.glob('FH_?.*')):
    #     print(name)
    
    
    #List filenames having third character as 'e'
    for name in sorted(glob.glob('??e*.*')):
        print(name)
       
            
# Use a character range ([a-z]) instead of a question mark
# to match one of several characters
def listMatchingRange():   
    # list of names ending with either 7/8/9
    # for name in sorted(glob.glob('*[7-9].*')):
    #     print(name)
    
    #List all name starting with either w,x,y,z
    for name in sorted(glob.glob('[w-z]*.*')):
        print(name)
 
def listRecursively(dir_path:str):
    for name in glob.glob(dir_path+"\**",recursive=True):
        print(name)
    
# iglob() : 
#Return an iterator which yields the same values as glob() without actually storing them all simultaneously.
#when to use it : When the listing is very large
def listUsingGenerator():
    
    fileNameGenerator = glob.iglob("a*.py") 
    print("return type of iglob() :",type(fileNameGenerator))
    
    for filename in fileNameGenerator:
        print(filename)
    
# escape() method
# It allows for escaping the given character sequence. You can find it handy for locating files with certain characters in their file names.
def escapeDemo():
    char_seq = "-_#"
    for spcl_char in char_seq:
        esc_set = "*" + glob.escape(spcl_char) + "*.*"
        for py in (glob.glob(esc_set)):
            print(py)
    
    
if __name__ == '__main__':
    dir_path = "D:\Python\Programs\pack"
    # listCurrentDirectory()
    
    # listFileInSpecifiedDirectory(dir_path)
#    print()
    # listSpecificFiles()
#    print()
    # listMatchingRange()
    # listRecursively(dir_path)
    # listUsingGenerator()
    # escapeDemo()
    
    