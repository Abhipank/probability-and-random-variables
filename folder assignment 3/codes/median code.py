
import pandas as pd


table=pd.read_excel("C:/Users/HP/Downloads/data.xlsx",skiprows=1,index_col=1)



items=table['Points scored by team']

from numpy import median as median
print(median(items))
import numpy as np
import matplotlib.pyplot as plt
X=list(items)
Y=(table['Match no.'])

print(X)
print(Y)
x1=np.linspace(0,50,1000)
y1=np.linspace(0,20,1000)
plt.plot(Y,X,marker='o',label='points scored')
plt.axhline(y=14,c='orange',linestyle='--',label='y=14')
plt.axhline(y=10,c='orange',linestyle='--',label='y=10')
plt.axhline(y=12,c='green',label='y=12 representing the median"12"')

#plt.scatter(X,Y,marker='o',label='Points scored by team')
plt.grid()
plt.legend()
plt.show()