# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:49:54 2020

@author: Varun Kapoor
"""

"""
1. Create the below pattern using 
nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
print("1.")
for x in range(1,5):
    print("*" * x)
for x in range(9):
    for y in range(5-x):
        print("*", end = "")
    print()
print()
    
"""
2. Write a Python program to reverse 
a word after accepting the input from 
the user.
"""
print("2.")
string = input("Please enter input: ")
print(string[::-1])