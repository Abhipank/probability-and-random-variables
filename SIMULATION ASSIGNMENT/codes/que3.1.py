
import numpy as np
import matplotlib.pyplot as plt


randvar=np.loadtxt("exp.dat",dtype="double")

err=[]

x=np.linspace(-4,4,50)
simlen=int(1e6)
for i in range(0,50):
  err_ind=np.nonzero(randvar <x[i]) #BTW nobody is zero otherwise they have been included
  err_i=np.size(err_ind)
  err.append(err_i/simlen)
  
plt.plot(x,err,"or")
plt.plot(x,err)
plt.grid()


plt.xlabel("$x$")
plt.ylabel("$F_X(x)$")

plt.savefig("exp_dis.pdf")
plt.savefig("exp_dis.eps")
