# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:10:55 2021

@author: Akash
"""

#Old and New Style of Formatting

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))


print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

#give placeholders an explicit positional index.
print('{1} {0}'.format('one', 'two'))
print('{1} {0} {1}'.format('one', 'two'))
print()

#Padding and aligning strings
#The old style defaults to right aligned 
print('%10s' % ('test',))
#while for new style it's left.
print('{:10}'.format('test'))  #default left
print('{:>10}'.format('test')) # Right aligned

#Align left:
print('%-10s' % ('test',))
print('{:10}'.format('test'))

#new style formatting provids more control 
#over how values are padded and aligned.

print('{:#<10}'.format('test'))
print('{:#^10}'.format('test')) # Center Alignment

#When using center alignment where the length of 
#the string leads to an uneven split of the padding 
#characters the extra character will be placed on 
#the right side
print('{:^6}'.format('zip'))

#Truncating long strings
print('%.5s' % ('xylophone',))
print('{:.5}'.format('xylophone'))

#Combining truncating and padding
print('%-10.5s' % ('xylophone',))
print('{:#<10.5}'.format('xylophone'))

#Numbers
print('%4d' % (42,))
print('{:4d}'.format(42))

# precision for floating point numbers limits the 
# number of positions after the decimal point.
print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))

#Padding
print('%04d' % (42,))
print('{:04d}'.format(42))

#Signed numbers
#By default only negative numbers are prefixed with a sign.
print('%d' % (42,)) #default
print('%d' % (-42,))

print('%+d' % (42,))
print('{:+d}'.format(42))

#New style formatting is also able to control the position of the sign symbol
# relative to the padding.
print('{:=5d}'.format((-   23)))
print('{:=+5d}'.format(23))

#Named placeholders
#Both formatting styles support named placeholders.
data = {'first': 'Karan', 'last': 'singh!'}
print('%(first)s %(last)s' % data)
print('{first} {last}'.format(**data))
print('{first} {last}'.format(first='Karan', last='Singh!'))

print('{first:#>10} {last:#<10}'.format(first='Karan', last='Singh!'))
    
print('{:b}'.format(10))
print('{:d}'.format(0x64))




num = 65535

print('Dec : %d' % num)  ## Dec
print('Dec :',format(num,"d"))

formatted_output = format(num,"d")
print('Dec :',formatted_output)

#  %x format specifier to convert an int value to a string and to 
#  represent it as a hexadecimal number:
print('Hex : %#x' % num)  # Hex
print('Hex :', format(num,"x"))

print('Oct : %#o' % num)  # Oct
print('Oct :',format(num,"o"))

print('Bin : %b' % num)  # Bin #Error
print(format(15, 'b')) # Binary
print(format(10, '#b')) # Binary
print(format(55, '#b')) # Binary

# print along with base
num = 2000
print('Hex with base : %#x' % num)  # HEx
print('Hex with base :',format(num,"#x")) # HEx

print('Oct with base : %#o' % num)  # Oct
print('Oct with base :',format(num,"#o")) # Oct
print('Bin with base :',format(num,"#b"))
      
roll = 9
sname   = "Sujay"

print("RollNo: %d\tName : %s" % (roll, sname))

print("RollNo:", format(roll,"d"), "\tName :",format(sname,"s"))


# integers
print(format(-10, '+')) # With sign
print(format( 10, '+')) # With sign

# Width specifier
print(format(55, '10d')) # width Without sign
print(format(55, '+10')) # width With sign
#sign alignment
print(format(55, '=+10'))
print(format(55, '=+010'))
print(format(55, '*=+10'))
print(format(55, '#=+10'))


#Alignment
# make a string center-aligned , '^' symbol
print(format("Hello", "#^15s"))
print(format("Goodday!", "#^15s"))

# align the target string from the left,  ‘<‘ symbol.   
print(format("Hello", "#<10s"))

# align the target string from the right,  ‘>‘ symbol.   
print(format("Hello", "#>10s"))

# pad internal blank spaces to numeric values
num = 55
print(format(num, '#=+10'))
num = -55
print(format(num, '#=+10'))
print(format(num, '*=+10'))
print(format(num, '*^+10'))
print(format(num, '*<+10'))
print(format(num, '*>+10'))

# float
print(format(0.20, '%')) # X 100
print(format(0.10, '%')) # X 100
print(format(45, '%'))

print(format(10.5, 'e'))
print(format(10.5, 'E'))
print(format(10500000, 'e'))
print(format(10500000, 'E'))
print(format(10500000, 'g'))
print(format(10500000, 'G'))

print(format(10.5345679, 'f'))
print(format(10.5345679, 'F'))

print(format(10.5345679, '10.2F'))
print(format(10.5345679, '010.2F'))
