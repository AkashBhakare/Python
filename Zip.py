# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:53:48 2021

@author: Akash
"""

a = range(1, 6)
b = range(10, 51,10)

for element in a:
    print(element)
    
for element in b:
    print(element)

# access both the range in parallel

for index in range(0,5):
    pair = (a[index],b[index])
    print(pair)


# From sequences to a sequence of tuples
a = range(0, 5)
b = range(15, 20)
c = range(25, 30)
print('List 1:',list(a))
print('List 2:',list(b))
print('List 3:',list(c))

sequence_of_tuples = zip(a, b, c)
print("Sequence of tuples:")
for item in sequence_of_tuples:
   print(item)

for item in sequence_of_tuples:
    (x,y,z) = item # unpack the tuple
    print(x,y,z)

nameList  = ['Raja','Rani','Sunny','Pintu']
scoreList = [ 77,    88,    91, 76]
studentRec = zip(nameList,scoreList)
for rec in studentRec:
    (name,mark) = rec #unpack tuple
    print('Name:',name,'\tMarks:',mark)

# dictionary construction with zip
myDict = dict()
studentRec = zip(nameList,scoreList)
for rec in studentRec:
    (name,mark) = rec #unpack tuple
    myDict[str(name)] = str(mark) # insert record in dictionary

print('Using Dictionary')
for key in myDict:
     print('Name:',key,'\tMarks:',myDict[key])

name = input('Please enter the student name:')
if name in myDict.keys():
    score = myDict.get(name)
    print(name, 'has secured',score,'marks')
else:
    print('No record found for ',name)

list1 = [('a',1),('b',2),('c',3)]
list2 = [('AAA',111),('BBB',222),('CCC',333)]
list3 = zip(list1,list2)
for item in list3:
    print("\nTuples:",item)
    ((a,b),(c,d)) = item
    print("After Unpacking :",a,b,c,d)
