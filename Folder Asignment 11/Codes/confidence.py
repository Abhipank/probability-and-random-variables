import numpy as np
import scipy.stats as st 

#define confidence level as alpha 
alpha=0.9
#define mean as loc 
loc=25000
#define standard error as scale 
scale=5000/8

#value of test statistic python is calculation itself
print(st.norm.interval(alpha,loc,scale))



