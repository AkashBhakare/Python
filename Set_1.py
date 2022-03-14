# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:24:27 2021

@author: Akash
"""

# understand data structure set
# Creates set with three items
# Set can be defined with curly braces({});
bri = {'India', 'Brazil', 'Russia', 'India'}
print("Type : ", type(bri))
print("BRI Countries are : ", bri)

#We can create a set using an iterable : set (<iter>)
s = set("helloo!")
print(s)

bri = {} #creates empty dictionary
print("Type : ", type(bri))

bri = set() # creates empty set
print("Type : ", type(bri))
print("BRI countries are : ", bri)

bri.add("India")
bri.add("India")
bri.add("Russia")
bri.add("Brazil")
print("BRI countries are : ", bri)

#list
briList = ['Brazil', 'Russia', 'India','Russia']
print("Type of brilist : ", type(briList))
print("BRI countries are : ", briList)

#remove duplicates from list
bri = list(set(briList)) #Create a set from list
print("Type of briList :", type(briList))
print("BRI countries are : ", bri)

#Not allowed to mutable object to set
bri.add(briList)

s = set(1,2,3) # Error : Expecting only one arguments
s = set(3)     # Error : Exceptes an iterable
s = ([1,2,3])
#List is iterable so can be supplied to set()
quadset = set(["USA", "JAPAN", "INDIA", "AUSTRALIA"])

bri.add(quadSet) #Error : QuadSet not hashable
print("After adding QUAD :",bri,sep='\n')

bri = set(['Brazil', 'Russia', 'India', 'Russia'])
print("Type of briList :", type(briList))
print("BRI countries are : ", bri)

# check existance in the set
if 'India' in bri:
    print('India is a member of BRI')
    
if 'USA' in bri:
    print('USA is a member of BRI')
else:
    print('USA is member of BRI')
    
print('Brazil is member of bri :',('Brazil' in bri))

bri_copy = bri   #shallo Copy
print("BRI Countries are :", bri)
print("BRI Countries are :", bri_copy)
print("BRI Countries are :", id(bri))
print("BRI Countries are :", id(bri_copy))
bri.add("SA")
print("BRI Countries are :", bri)
print("BRI Countries are :", bri_copy)

bri = set(['Brazil', 'Russia', 'India', 'Russia'])
# Create copy of the existing set
bric = bri.copy() #Deep copy
print("BRI Countries are :", bri, id(bri))
print("BRIC Countries are :", bric, id(bric))
bri.add("SA")
print("BRI Countries are :", bri)
print("BRI Countries are :", bric)

# add new element to the set
bric.add('China')
print("BRI Countries are :", bric)
print("BRI Countries are : ",bri)

#delete element from the set
bric.remove('Russia')
print("BRIC Countries are : ", bric)
print("BRI Countries are :", bri)
print('is bric superset of bri :',bri.issuperset(bri))
print('is bric superset of bric :',bric.issuperset(bric))

bric.add('Russia')
print('is bri superset of bri :',bri.issuperset(bri))
print('is bric superset of bric :',bric.issuperset(bric))

set1 = set([1,3,4,7])
set2 = set([5,4,7,2])

print("Set1 ", set1)
print("Set2 ", set2)

print('Union', set1.union(set2))
print("Set1 ", set1)
print("Set2 ", set2)

print('Union', (set1 | set2) )
print("Set1 ", set1)
print("Set2 ", set2)

print('Intersection', set1.intersection(set2))
print("Set1 ", set1)
print("Set2 ", set2)

print('Difference', set1.difference(set2))
print("Set1 ", set1)
print("Set2 ", set2)

print('Difference', (set2-set1))
print("Set1 ", set1)
print("Set2 ", set2)

print('Symm Difference', set1.symmetric_Difference(set2))

set1 = set([1,3,4,7])
set2 = set([5,4,7,2])
print('Symm Difference', (set1^set2))

set1 = set([1,3,4,7])
set2 = set([5,4,7,2])

#Intersection_update will update a set with the intersection of
print('Intersetion_update', set1.intersection_update(set2))
print("Set1 ", set1)
print("Set2 ", set2)

set1 = set([1,3,4,7])
set2 = set([5,4,7,2])
#Update a set1 with the union of itself and set2
set1.update(set2)
print("Set1 ", set1)
print("Set2 ", set2)

#isdisjoint : This method will return True if two sets have a null intersectior
s1 = {1,2}
s2 = {1,2,4}
s3 = {5,7}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

#issubset : This is method reports whether another set contains this set.
s1 = {1,2}
s2 = {1,2,4}
print("is s1 subset s2 ? ",s1.issubset(s2))

print("is s1 PURE subset s2 ? ",s1 < s2) # pure

print("is s2 subset s1 ? ",s1.issubset(s1))
print("is s2 PURE subset s1 ? ",s2 < s1) 

s1 = {1,2,4}
s2 = {1,2,4}
print("is s1 subset s2 ? ",s1.issubset(s2))
print("is s1 PURE subset s2 ? ",s1 < s2) # pure

#issuperset : This method will report whether this set
# contains another set.
s1 = {1,2,4}
s2 = {1,2,4}
print("is s2 subset s2 ? ",s2.issubset(s1))
print("is s2 PURE subset s2 ? ",s2 > s1) 

print("is s1 subset s2 ? ",s1.issubset(s2))
print("is s1 PURE subset s2 ? ",s1 > s2) 

#discard 
#Removes an element from a set if it is a member.
#If the element is not a member, do nothing.
saarc = {"Ïndia", "Pakistan", "Bangladesh","Nepal",
         "Bhutan", "Maldives", "Srilanka"}
print("SAARC : ", saarc,sep="\n")
saarc.discard("pakistan")
saarc.discard("Pakistan")
print("SAARC :", saarc)

#remove
#Removes an element from a set if it is a member.
#If the element is not a member, raises keyError.
saarc.remove("Nepal")
print("SAARC : ", saarc)
saarc.remove("Nepal")

# removes all elements from the set
saarc .clear()
print("SAARC : ",saarc)

#Removes a random element from a set.
x = {'abcd', 'foo', 'bar', 'baz'}
print(x.pop())
print(x)
x.clear()
print(x)
print(x.pop()) #Pop from empty set raise exception

#set union can be perfromed with the | operator
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quax'}
print("Union:", x1 | x2)

#More than two sets may be specified with either the operator or the method
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print("union:", a.union(b, c, d))
print("Union :", a | b | c | d)

#Intersection using operator and function
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print("Intersection :", x1.intersection(x2))
print("Intersection :", x1 & x2)

# you can specify multiple sets with the intersection method and operator
print("Intersection :", a.intersection(b, c, d))
print("Intersection :", a - b - c - d)

# x1.symmetric_difference(x2) and x1 ^ x2
# return the set of all element in either x1 or x2, but not both:
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print("sym Diff :",x1.symmtric_difference(x2))
print("Sym Diff :", (x1 ^ x2))

s = {"India", "Russia", "Brazil","China"}
print(s)
s = sorted(s)
print(s)




















