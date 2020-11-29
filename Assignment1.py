# Varun Kapoor

# Problem 1
"""
1. Write a program which will find all 
such numbers which are divisible by 7 
but are not a multiple of 5, between 
2000 and 3200 (both included). The 
numbers obtained should be printed
in a comma-separated sequence on a 
single line.
"""
print("1. ")
s = ""
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        s = s + str(i) + ","
print(s[:-1])
print()

# Problem 2
"""
2. Write a Python program to accept 
the user's first and last name and 
then getting them printed in the the 
reverse order with a space between 
first name and last name.
"""
print("2. ")
first = input("Enter First Name: ")
last = input("Enter Last Name: ")
print(first[::-1], last[::-1])
print()

# Problem 3
"""
3. Write a Python program to find the 
volume of a sphere with diameter 12 cm.
"""
print("3. ")
diameter = 12
radius = diameter/2
volume = (4/3) * 3.14 * (radius ** 3)
print(volume)