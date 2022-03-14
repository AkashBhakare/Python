# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:20:21 2021

@author: Akash
"""

#matrix addition in python
rows = int(input("=Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)

print("Enter the elements of Second Matrix:")
matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
for n in matrix_b:

    print(n)
    
result=[[0 for i in range(column)] for i in range(rows)]

for i in range(rows):
    for j in range(column):
        result[i][j] = matrix_a[i][j]+matrix_b[i][j]

print("The Sum of Above two Matrices is : ")
for n in result:
    print(n)
    
    
    

    
    
    
    
    
                        
                    
X = [[1, 3], [4,5], [7, 9]]

result = [[X[j][i] for j in range (len (X))] for i in range (len (X[0]))]

for r in result:

              print (r)
    
    
    
    
    
    
    
    
    
    
    
    
    
    