# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:17:12 2021

@author: Akash
"""

import sys
import time

def readFile():
    filename = input("Enter the name of the file to read :")
    fileObject = open(filename,"r")
    print("Press ctrl+c now to stop reading\n")
    # Our usual file- reading odiom
    while True:
        line = fileObject.readline()
        #print("length : ",len(line))
        if len(line) == 0:
            break  #terminates loops
        print(line, end='')
        sys.stdout.flush()
        #To make sure it runs for a while
        time.sleep(1)
        
def readFile():
    fileObject = None
    
    try:
        filename = input("Enter the name of the file to read :")
        fileObject = open(filename, "r")
        print("Press Ctrl+c now to stop reading\n")
        # Our usual file-reading idiom
        while True:
            line = fileObject.readline()
            #print("Length : ",len(line))
            if len(line) == 0:
                break  #terminates Loops
            print(line, end='')
            sys.stdout.flush()
           # To make sure it runs for a while
            time.sleep(1)
    except FileNotFoundError :
        print(f"file '{filename}' not found\n")
    except IOError as err:
        print("Error : ",err)
    except KeyboardInterrupt :  # When Ctrl+c is pressed
        print("\n!! You cancelled the reading from the file.")
    except EOFError:     # When Ctrl+d is pressed
        print('Why did you do an EOF on me?')
    except UnicodeDecodeError:
        print("The unicode characters in this file could not be read!\n")
    finally:
        if fileObject:
            fileObject.close()
            print("\n(Cleaning up: Closed the file)")
        print("visited Finally")
        
                              

if __name__ == 'main':
     readFile()
   #readFile()
    # readFile1()
    # readFile2()
















