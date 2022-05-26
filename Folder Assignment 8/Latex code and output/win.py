

#python code 


import numpy as np


#using python library to achieve binomial distribution probability
from scipy.stats import binom



#setting the value of n
n=float(input("Enter the value of n: "))


#setting the value of p
p=float(input("Enter the value of p: "))

A=n*p
print("E[X]= ",A)

B=n*(n-1)*p*p
print("E[X(X-2)]= ",B)


C=n*(n-1)*(n-2)*p*p*p
print("E[X(X-1)(X-2)]= ",C)

D=n*(n-1)*p*p+n*p
print("E[X^2]= ",D)

F=n*(n-1)*(n-2)*p*p*p+3*n*(n-1)*p*p+n*p
print("E[X^3]= ",F)


