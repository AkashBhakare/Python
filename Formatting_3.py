# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:44:30 2021

@author: Akash
"""

# Old and New Style of Formatting

print('the values are %s %s' % ('one', 'two'))
print('the values are  {} {}'.format('one', 'two'))
s = 'the values are {} {}'.format('one', 'two')
print(s)

#number of placeholders should not be more than the arguments
print('the values are {} {} {}'.format('one', 'two')) #Error
#number of placeholders can be less than the arguments
print('the values are {} {}'.format('one','two','three')) #okay
print('the values are {}, {} and {}'.format('one','two','three'))


print('%d, %d' % (11, 12))
print('{}, {}'.format(11, 12))

# give placeholders an explicit positional index.
print('{1} {0}'.format('one', 'two'))

print('{1} {0} {1}'.format('one', 'two'))

print('{1} {0} {2}'.format('one', 'two'))

rec = (9,"Raja")
print("{0},{1}".format(rec))

print("{0}, {1}".format(9,"Raja"))
print("{1}, {0}".format(9,"Raja"))
print()

# str.format() returns a formatted string
value = 1234.56789
data = "my value is |{0:10.2f}| |{0:15.3f}|".format(value)
print(data)

# Padding and aligning strings

# The old style defaults to right aligned 
print('|%10s|' % ('test',))

# str.format the default justifcation is left for string.
print('|{:10}|'.format('test'))  # default left
print('|{:>10}|'.format('test')) # Right aligned
print('|{:^10}|'.format('test')) # Center aligned
print('|{:<10}|'.format('test')) # Left aligned

# str.format the default justifcation is right for numeric.
print('|{:10}|'.format(555)) 
print('|{:10.2f}|'.format(555.666))

# Align left:
print('|%10s|' % ('test',))  # default right in old style
print('|%-10s|' % ('test',))

print('|{:10}|'.format('test')) # default left in new style
print('|{:<10}|'.format('test'))
print('|{:>10}|'.format('test'))

#new style formatting provids more control 
#over how values are padded and aligned.

print('{:#<10}'.format('test')) # Left alignment
print('{:#^10}'.format('test')) # Center Alignmenttest
print('{:#>10}'.format('test')) # Right Alignment

# When using center alignment where the length of 
# the string leads to an uneven split of the padding 
# characters the extra character will be placed on 
# the right side
print('|{:^10}|'.format('zip'))
print('|{:~^10}|'.format('zip'))

# Truncating long strings
print('%.5s' % ('xylophone',))
print('{:.5}'.format('xylophone'))

# Combining truncating and padding
print('|%-10.5s|' % ('xylophone',))
print('|{:10.5}|'.format('xylophone'))
print('|{:<10.5}|'.format('xylophone'))
print('|{:#>10.5}|'.format('xylophone'))
print('|{:#<10.5}|'.format('xylophone'))
print('|{:#^10.5}|'.format('xylophone'))

# Numbers
print('|%4d|' % (42,))
print('|{:4d}|'.format(42))

# precision for floating point numbers limits the
# number of positions after the decimal point.
print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))

# Padding
print('Value = %04d' % (42,))
print('Value = {:04d}'.format(42))
print('Value = {:0>5d}'.format(42))

print('{:0<5d}'.format(42)) # Warn
print('{:0^5d}'.format(42)) # Warn
print('{:5^5d}'.format(42)) # Warn

print('{:#>5d}'.format(42))  #right
print('{:#^5d}'.format(42))  #center
print('{:#<5d}'.format(42))  #left

# Signed numbers
# By default only negative numbers are prefixed 
# with a sign.
print('%d' % (42,)) #default
print('%d' % (-42,))

print('%+d' % (42,))
print('%+d' % (-42,))

print('{:+d}'.format(42))
print('{:+d}'.format(-42))

# New style formatting is also able to control the position of the sign symbol
# relative to the padding.
print('{:=5d}'.format(-23))
print('{:=+5d}'.format(23))
print('{:0=5d}'.format(-23))
print('{:0=+5d}'.format(23))

# Named placeholders
# Both formatting styles support named placeholders.
data = {'first': 'Karan', 'last': 'singh'}
print('%(first)s %(last)s' % data)

print('{first} {last}'.format(**data))
print('{first} {last}'.format(first='Karan', last='Singh'))

print('{last:#>10} {first:#<10}'.format(first='Karan', last='Singh'))
print('{last:#>10} {first:#<10}'.format(**data))

fstr = '{first} {last}'.format(**data)
print(fstr)
print(fstr.upper())

print('{:b}'.format(100))
print('{:#b}'.format(0x64))
print('{:#o}'.format(0x64))
print('{:d}'.format(0x64))


# The datetime module supplies classes for 
# manipulating dates and times.
# using type-specific formatting:
import datetime
d = datetime.datetime(2021, 8, 31, 20, 37, 58)
print(d)
print('{:%Y-%m-%d}'.format(d))
print('{:%H:%M:%S}'.format(d))

d = datetime.datetime.now()
print('{:%Y-%h-%d %H:%M:%S}'.format(d))

now = datetime.date.today()
print(now)
print('{:%h %d, %Y }'.format(d))

t = datetime.time(5,16,56)
print(t)
print('{:%H-%M-%S}'.format(t))


amt = 1000000
print("Rs:",amt)
print("Rs {:,d}".format(amt))
print("Rs {:,}".format(amt))

