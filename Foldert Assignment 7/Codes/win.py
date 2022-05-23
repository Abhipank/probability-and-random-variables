
import numpy as np
#using python library to achieve binomial distribution probability
from scipy.stats import binom
#setting values
m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))
p=float(input("Enter the value of p: "))
q=1-p
#creating a list of integers from 0 to n-1
lst=list(np.arange(0,n))

sum=0
#finding the probability
for x in lst:
  sum=sum+binom.pmf(m-1,m+x-1,p)*p

print(sum)
