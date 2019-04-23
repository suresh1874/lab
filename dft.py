import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

#x=input("Enter i/p sequence : ")
x=[1,2,3]
'''z=input("Enter No of Zeros : ")
y=np.zeros(z)
x=np.append(x,y)
print(x)'''


j=np.complex(0,1)
X = []
N = len(x)
for k in range(0,N):
   	y = 0
   	for n in range(0,N):
   		y+= x[n]*np.exp((-2*j*np.pi*k*n)/N)
   	print(y)
   	X.append(y)
print(X)
plt.stem(X)
plt.show()


#lin,time shift,conv,parsvels theorem
