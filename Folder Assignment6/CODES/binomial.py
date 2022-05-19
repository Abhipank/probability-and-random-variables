


#using python library to achieve binomial distribution probability
from scipy.stats import binom
#setting value of n i.e. no of trials
n=5
#setting value of parameter i.e. probability of getting spade in each draw
p=1/4



#for (i) solution
r=5

solution_i=binom.pmf(r,n,p)
print("solution (i) = " ,solution_i)


#for (i) solution
r=3

solution_ii=binom.pmf(r,n,p)
print("solution (ii) = " ,solution_ii)

#for (i) solution
r=0

solution_iii=binom.pmf(r,n,p)
print("solution (iii) = " ,solution_iii)
