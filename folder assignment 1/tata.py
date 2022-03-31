import numpy as np
from matplotlib import pyplot as plt


x=[0, 1, 2, 3, 4, 5]
y=[0, 0, 0, 0, 0, 0]



plt.plot(x,y,'r*')


x=np.linspace(-6,6,100)


plt.axvline(x=0,c="black",label='x=0')
plt.axhline(y=0,c="black",label='y=0')
#plt.axvline(x=-2,c='black',label='x=-2')
#plt.axvline(x=5,c='black',label='x=5')

#plt.plot(x,11*x-4,'-g',label='y=11*x-4')
#plt.plot(x,15*x+4,'-b',label='y=15*x+4')
#plt.plot(x,13*x+14,'-r',label='y=13*x+14')

plt.legend()
plt.grid()
plt.show()