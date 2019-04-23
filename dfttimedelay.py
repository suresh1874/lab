import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

#x=input("Enter i/p sequence : ")
'''z=input("Enter No of Zeros : ")
y=np.zeros(z)
x=np.append(x,y)
print(x)'''

x1=[1,2,3,4]
x2=[0,0,0,0,1,2,3,4]


def N_dft(x,N):
	j=np.complex(0,1)
	X = []
	#N = len(x)
	for k in range(0,N):
   		y = 0
   		for n in range(0,N):
   			y+= x[n]*np.exp((-2*j*np.pi*k*n)/N)
   		#print(y)
   		X.append(y)
	#print(X)
	return X


X1=N_dft(x1,4)
X2=N_dft(x2,8)

X1mag=np.abs(X1)
X2mag=np.abs(X2)


X1phase=np.angle(X1)
X2phase=np.angle(X2)


plt.subplot(411)
plt.ylabel('X1 magnitude')
plt.stem(X1mag)
plt.subplot(412)
plt.ylabel('X2mag Delayed version')
plt.stem(X2mag)
plt.subplot(413)
plt.ylabel('X1 Phase')
plt.stem(X1phase)
plt.subplot(414)
plt.ylabel('X2 Phase Delayed')
plt.stem(X2phase)
plt.show()