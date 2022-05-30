import numpy as np
import matplotlib.pyplot as plt


coordinates = np.loadtxt('pdef.dat', dtype='float')
X = []
Y = []
for coordinate in coordinates:
    X.append(coordinate[0])
    Y.append(coordinate[1])

x= np.linspace(0, 6, 100)

plt.plot(X,Y, label='$f(z)=2z-2-2lnz$')

plt.axvline(x=0,c="black",linestyle='--',label="x-axis")
plt.axhline(y=0,c="black",linestyle='--',label="y-axis")


plt.grid()
plt.legend()
plt.show()