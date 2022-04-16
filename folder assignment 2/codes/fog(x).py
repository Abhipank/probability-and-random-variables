import numpy as np
import matplotlib.pyplot as plt


coordinates = np.loadtxt('fog(x).dat', dtype='float')
X = []
Y = []
for coordinate in coordinates:
    X.append(coordinate[0])
    Y.append(coordinate[1])

x= np.linspace(-6, 6, 100)

plt.plot(X,Y, label='$fog(x)=8x^6+12x^4+6x^2+1$')

plt.axvline(x=0,c="black",linestyle='--',label="x-axis")
plt.axhline(y=0,c="black",linestyle='--',label="y-axis")


plt.grid()
plt.legend()
plt.show()