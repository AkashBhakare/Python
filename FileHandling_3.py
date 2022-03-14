# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:07:10 2021

@author: Akash
"""

# Open a file for writing
fo = open("B:\\Python_Impetus_Code\\abc.txt", "w")
string = "Python is a great language.\nYeah its great!!\n"
fo.write( string )
# Close opend file
fo.close()
        
#open file for reading
fo = open("B:\\Python_Impetus_Code\\abc.txt", "r")

string = ""
#read from file
string = fo.read();
print(f"file content is :\n\t{string}")

#close file
fo.close()


fo = open("B:\\Python_Impetus_Code\\abc.txt", "w")
string = "I love Python!"
fo.write( string )
# Close opend file
fo.close()
