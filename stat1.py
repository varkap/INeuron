# Problem 1
arr = [6, 7, 5, 7, 7, 8, 7, 6, 9, 7, 4, 10, 6, 8, 8, 9, 5, 6, 4, 8]
mean1 = sum(arr)/len(arr)

# Problem 2
arr2 = [28, 122, 217, 130, 120, 86, 80, 90, 140, 120, 70, 40, 145, 113, 90, 68, 174, 194, 170,
100, 75, 104, 97, 75,
123, 100, 75, 104, 97, 75, 123, 100, 89, 120, 109]
mean2 = sum(arr2)/len(arr2)

# Problem 2
x = [0, 1, 2, 3, 4, 5]
fx =[0.09, 0.15, 0.40, 0.25, 0.10, 0.01]
a = []
for i in range(len(x)):
    a.append(x[i] * fx[i])
mean3 = sum(a)

# Problem 6
g5 = (.75 ** 5) * (.25 ** 3)
b5 = (.45 ** 5) * (.55 ** 7)
g4 = (.75 ** 4) * (.25 ** 4)
b6 = (.45 ** 6) * (.55 ** 6)
import matplotlib.pyplot as plt
plt.bar([1,2], [g5,g4])
plt.bar([1,2], [b5,b6])
# From this we can infer that Gaurav has a higher
# likelihood of passing the entrance exam. The two main
# governing factors are the correction rate and the number
# of questions practiced per day

#Problem 7
import numpy as np
def lambda_func(k, lamb):
    factorial = 1
    for i in range(2, k+1):
        factorial = factorial * i
    return (lamb ** k) * (np.e ** (0 - lamb) / factorial)
    
lambda7 = 72 * 4/60
five = lambda_func(5, lambda7)
three = lambda_func(0, lambda7) + lambda_func(1, lambda7) + lambda_func(2, lambda7)
morethree = 1 - three

# Problem 8
two8 = lambda_func(2, (455/77)/10)

# if the number of words increases, then lambda increases, and
# versa

# The probability of maknig a number of errors 
# will be increase if the number of words increase

# Problem 9 is a repeateed question to problem 4

# Problem 10
# a.i.   1 - 0.8962 = 0.1038
# a.ii.  0.1949
# a.iii. 1 - 0.0853 = 0.9147
# a.iv.  6443 - .1056 = 0.5387
# a.v.   0
# b.     z = 1.6449
# c.     z = 2.5758

# Problem 11
# i.   p(z>1.5) = 0.0668
# ii.  P(Z < 1) - P(Z < -1) = 0.8413 - 0.1587 = 0.6826
# iii. ( x - 10) / 2 = 2.0537
#      x = 14.1074

# Problem 12
# i.   0.9192
# ii.  0.9973