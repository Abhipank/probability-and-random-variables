import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as linalg


#line 1 --> 11x-y = 4
#line 2 --> 15x-y =-4
#line 3 --> 13x-y = -14


A=np.array([[11,-1],[15,-1]])
B=np.array([4,-4])
X_1=np.linalg.solve(A,B);
print("THE INTERSECTION POINT OF LINE 1 AND LINE 2 :")
print(X_1)

A=np.array([[15,-1],[13,-1]])
B=np.array([-4,-14])
X_2=np.linalg.solve(A,B);
print("THE INTERSECTION POINT OF LINE 2 AND LINE 3 :")

print(X_2)



	#here plt can be directly below plt
x=np.linspace(-6,6,100)# when it was bnefore zip line not plt text was shown may be due change of x #points plot and in npspace x is changing

plt.axvline(x=0,c="black",label='x=0')
plt.axhline(y=0,c="black",label='y=0')
plt.axvline(x=-2,c='black',linestyle='--',label='x=-2')
plt.axvline(x=5,c='black',linestyle='--',label='x=5')

plt.plot(x,11*x-4,'-g',label='y=11*x-4')
plt.plot(x,15*x+4,'-b',label='y=15*x+4')
plt.plot(x,13*x+14,'-r',label='y=13*x+14')

x=[0, 1, 2, 3, 4, 5]
y=[0, 0, 0, 0, 0, 0]



#plt.plot(x,y,'r.',s=20)

plt.scatter(x,y,s=150)


for i,j in zip(x,y) :
    plt.text(i,j,'({},{})'.format(i,j))
	

plt.legend()
plt.grid()
plt.show()