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
x2=[1,2,3,4]
x3=[]
for x in xrange(0,len(x1)):
	y=x1[x]+x2[x]
	x3.append(y)

def N_dft(x,N):
	j=np.complex(0,1)
	X = []
	N = len(x)
	for k in range(0,N):
   		y = 0
   		for n in range(0,N):
   			y+= x[n]*np.exp((-2*j*np.pi*k*n)/N)
   		#print(y)
   		X.append(y)
	#print(X)
	return X


X1=N_dft(x1,4)
X2=N_dft(x2,4)
X3=N_dft(x3,4)
X1mag=np.abs(X1)
X2mag=np.abs(X2)
X3mag=np.abs(X3)
X1X2mag=X1mag+X2mag


#Xphase=np.angle(X2)

plt.subplot(411)
plt.ylabel('X1mag')
plt.stem(X1mag)
plt.subplot(412)
plt.ylabel('X2mag')
plt.stem(X2mag)
plt.subplot(413)
plt.ylabel('X3mag')
plt.stem(X3mag)
plt.subplot(414)
plt.ylabel('X1+X2 mag')
plt.stem(X1X2mag)
plt.show()