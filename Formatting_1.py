# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:54:11 2021

@author: Akash
"""

# %s format specifier here to tell Python where to 
# substitute the value of name, represented as a string.
name = "Sujay"
data = 'Hello, %s' % name
print(data)

num = 65535
print('Dec : %d' % num)  ## Dec
#  %x format specifier to convert an int value to a string and to 
#  represent it as a hexadecimal number:
print('Hex : %x' % num)  ## Hex
print('Oct : %o' % num)  ## Oct
#print('Bin : %b' % num)  ## Bin

# print along with base
print('Hex with base : 0x%x' % num)  ## HEx
print('Oct with base : 0o%o' % num)  ## Oct
# print along with base
print('Hex with base : %#x' % num)  ## HEx
print('Oct with base : %#o' % num)  ## Oct
      
rollNo = 9
Name = "Sujay"

print("RollNo: %d\tName :%s" %(rollNo,name))

#passing a single tuple as argument
record = (10,"Karan")
print("RollNo: %d\tName :%s" %record)

# positional argument
print("RollNo: %d\tName :%s\tRollNo %d" %(rollNo,name,rollNo))
# keyword argumennt
print("RollNo: %(val)d\tName :%(name)s\tRollNo %(val)d" \
                                          %{"val":rollNo,"name":name})
# keyword argument : order or argument does not matter
print("RollNo: %(num)d\tName :%(sname)s" %{"sname":name,"num":rollNo})

# Minimum widht Specifier
print("Name :%10s"%(name))

#Controlling Precision 
real = 1234.5678905
print("Real number = ",real)
print("Real number = %f "%real)
print("Real number = %.2f "%real)
print("Real number = %10.2f "%real)
print("Real number = %f "%real)

real = 120000000000.0

print("Real Number =",real)
print("Real Number = %F"%real)
print("Real Number = %f"%real)
print("Real Number = %e"%real)
print("Real Number = %E"%real)
print("Real Number = %g"%real)
print("Real Number = %G"%real)
real = 3.4
print("Real Number = %F"%real)
print("Real Number = %e"%real)
print("Real Number = %G"%real)

#  Character formatting
# using variable
ch = 'A'
print("Character = %c"%ch)

# using constant
print("Character = %c"% 'D')

# using code
ch = 88
print("Character = %c"% ch)
print("Character = %c"% 88)

# flag "+" in format directive to specify sign
num = -44
print("Number = %d"%num)
num = +44
print("Number = %d"%num)
num = +44
print("Number = %+d"%num)
num = -44
print("Number = %+d"%num)

# Padding space with 0
num = 44
print("Number = %5d"%num)
print("Number = %05d"%num)

# Left justification (default is right)
num = 44
print("Number = %5d"%num)
print("Number = %05d"%num)
print("Number = %-5d"%num)

# Precedes a positive number with a blank space
print("%d%d"%(-10,10))
print("% d% d"%(-10,10))
print("%   d%   d"%(-10,10))


#String % Dictionary

record = { 
           "Occupation": "Chef",
           "Name" : "Mohan", 
           "Income" : 40000 
        } 
# 
print("%(Name)s is a %(Occupation)s earning Rs"\
                      "%(Income)2.2f"% record )
# 
print("Income = Rs %(Income)2.2f"% record )



# %s format specifier here to tell Python where to 
# substitute the value of name, represented as a string.
name     = "Sujay"
string   = 'Hello, %s'
result   = string%name
print(result)

print("Hello ",name,", how are you ?", sep="")
print('Hello %s, How are you?' % name)
print('Hello %s, How are you?' % 'Gauri')

nameList = ["Sarthak", "Shardul", "Sneha", "Shraddha"]

for name in nameList:
    print("Hello %s, Good Evening!" % name)

playerList = ["Jui","Kapil","Harshal","Pranit"]
for name in playerList:
    print( "Hello, %s, How are you?" % name)
   
menuList = ["Poha","Upma","Idly","Dosa","Vada"]
for item in menuList:
    print("Enjoy delecious %s!" % item)

name     = "Sunita"
string   = 'Hello, %s'
print(string%name)

    
num = 65535
print('Dec : %d' % num)  ## Dec
#  %x format specifier to convert an int value to a string and to 
#  represent it as a hexadecimal number:
print('Hex : %x' % num)  # Hex
print('Oct : %o' % num)  # Oct
#print('Bin : %b' % num)  # Bin

# print along with base : inappropriate way : error prone
print('Hex with base : 0x%x' % num)  # HEx
print('Oct with base : 0o%o' % num)  # Oct

# print along with base
print('Hex with base : %#x' % num)  # Hex
print('Hex with base : %#X' % num)  # Hex
print('Oct with base : %#o' % num)  # Oct

num = 2000
print('Hex with base : %#x' % num)  # Hex
print('Hex with base : %#X' % num)  # Hex
      
rollNo = 9
name   = "Sujay"
print("RollNo: %d\tName :%s" % rollNo, name)
print("RollNo: %d\tName :%s" % (rollNo, name))

#passing a single tuple as argument
record = (10, "Karan")
print("RollNo: %d\tName :%s"    % record)
print("RollNo: %d\tName :%s %f" % record) # Error

# positional argument
print("RollNo: %d\tName :%s\tRollNo %d" % (rollNo, name, rollNo))

format_string = "%s's roll number is %d, %s stood first in the class"
print(format_string %('Sujay',12,'Sujay'))

rollNo = 9
name   = "Sujay"
# keyword argument (Mapping Key)
print("RollNo: %(r)d\nName :%(n)s\nRollNo %(r)d"% {"r" : rollNo,"n" : name})

format_string = "%(sname)s's roll number is %(roll)d, %(sname)s stood first in the class"

print(format_string % {"sname":name,"roll":rollNo})

print(format_string %{"sname":"Raja","roll":14})


# keyword argument : order or argument does not matter
print("RollNo: %(roll)d\tName :%(sname)s" %{"sname":name,"roll":rollNo})

sdict = {"name":"Sandesh","roll":13}
format_string = "RollNo: %(roll)d\tName :%(name)s"
print(format_string % sdict)

#List of Dictionary
records = [{"name":"Monika", "roll":13},
           {"name":"Priti",  "roll":15},
           {"name":"Vedant", "roll":16}]

format_string = "RollNo: %(roll)d\tName :%(name)s"

for a_record in records:
    print(format_string % a_record)
    
mydict = {"apt"  :"apporpriate for that situation",
          "slice":"Cut into pieces"}

print("1st words meaning : %(apt)s\n2nd words meaning : %(slice)s"%mydict)

# Not necessary to use all the keys from the dict
print("1st words meaning : %(apt)s"%mydict)


#Cannot mix the keyword and positional args
num = 999
print("Words meaning : %(apt)s\t%d"%(mydict,num))
print("num = %d\tWords:%(apt)s"%(num,mydict))

# Minimum width Specifier
name = "Rohit"
print("Name :|%s|"   % name)
print("Name :|%10s|" % name)
print("Name :|%3s|"  % name)
name = "Xu"
print("Name :|%3s|"  % name)

num = 99
print("Number:|%d|"  % num)
print("Number:|%5d|" % num)
print("Number:|%#5x|" % num)

import math
print(math.pi)  # 15
# %f : six digit precision 
print('|%f|'   % math.pi)   # 6
print('|%10f|' % math.pi) #minimum width specifier


# Controlling Precision
pi = math.pi
print("Real number = ", pi)
#Rounds the value upto six digit precision
print("Real number = %f "   % pi)
print("Real number = %.2f " % pi)
print("Real number = %.0f " % pi)

real = 1.6789
print("Real number = %.2f " % real)
print("Real number = %.0f " % real)

# using specifiers in combination
print("Real number= |%f|"       % pi)
print("Real number= |%10f|"     % pi)
print("Real number= |%.2f|"     % pi)
print("Real number= |%10.2f| "  % pi)


real = 120000000000.0

print("Real Number =",     real)
print("Real Number = %F" % real)
print("Real Number = %f" % real)
print("Real Number = %e" % real)
print("Real Number = %E" % real)
print("Real Number = %g" % real)
print("Real Number = %G" % real)
real = 3.4
print("Real Number = %F" % real)
print("Real Number = %e" % real)
print("Real Number = %G" % real)

real = 12300000000.0
print("Real Number = %e"   % real)
print("Real Number = %.2e" % real)
print("Real Number = %.4e" % real)

#  Character formatting
# using variable
ch = 'A'
print("Character = %c " % ch)

# using constant
print("Character = %c" % 'Q')     #char
print("Character = %c" % 136)     #int
print("Character = %c" % 1108)    #int
print("Character = %c" % 2309)  
print("Character = %c" % 136.67)  #real Error
print("Character = %c" % 'UML')   #String Error

# using code
val = 65
print("Character = %c" % val)
print("Character = %d" % val)
val = 'R'
print("Character = %c" % val)
print("Character = %d" % val) #error
print("Character = %d" % ord(val)) 

# flag "+" in format directive to specify sign
num = -44
print("Number = %d" % num)
num = +44
print("Number = %d" % num)
num = 44
print("Number = %+d" % num)
num = -44
print("Number = %+d" % num)

# Padding space with 0
num = 43
print("Number = |%5d|"  % num)
print("Number = |%05d|" % num)

# Left justification (default is right)
num = 43
print("Number = |%5d|"   % num)
print("Number = |%05d|"  % num)
print("Number = |%-5d|"  % num)
print("Number = |%-05d|" % num) 

name = "Raj"
print("Name:|%10s|"  %name)
print("Name:|%-10s|" %name)


# Precedes a positive number with a blank space
print("%d%d" % (-10, 10))
print("% d% d" % (-10, 10))
print("%   d%   d" % (-10, 10))
print("%d %d" % (-10, 10))
print("%d    %d" % (-10, 10))
# String % Dictionary

record = {
           "Occupation" : "Chef",
           "Name"       : "Mohan",
           "Income"     : 40000.34534
        }

print("%(Name)s is a %(Occupation)s earning Rs%(Income) -10.0f" % record)

print("Income = Rs %(Income)-13.2f" % record)
print("Income = Rs %(Income)3.2f"  % record)

per = 75.8975
print("My percentage score is %.2f%%" % per)

# width specifier supplied at runtime
num   = int(input("Enter a number:"))
width = int(input("How much width to use:"))
print("Value = |%*d|" % (width, num))

# width and precision specifier supplied at runtime
num       = float(input("Enter a real number:"))
width     = int(input("How much width to use:"))
pricision = int(input("What should be the precesion?"))

print("Value = %0*.*f" % (width, pricision, num))

product = [
        {"name": 'cy', "price" : 123456.7845},
        {"name": 'qwa', "price" :456.3244},
        {"name": 'tyme', "price" : 1456.38}
        ]


print("cy = ",123456.7845)
print("qwa = ",456.3244)
print("tyme = ",1456.38)
print("total = ",(123456.7845+456.3244+1456.38))

line = '-'*21
print(line)
print("   ***   Bill  ****")
print(line)
format_string = "%(name)-7s = %(price)10.2f"
total_price = 0
for record in product:
    print(format_string % record)
    total_price += record["price"]
    

format_string = "%-7s = %10.2f"
print(line)
print(format_string % ("Total",total_price))
print(line)