
import numpy as np
#using python library to achieve binomial distribution probability
from scipy.stats import binom

m=int(input("Enter the value of m: "))
n=int(input("Enter the value of n: "))
p=float(input("Enter the value of p: "))
q=float(input("Enter the value of q: "))

lst=list(np.arange(1,n))

sum=0

for x in lst:
  sum=sum+binom.pmf(m-1,m+x-1,p)*q

print(sum)