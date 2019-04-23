import numpy as np
import matplotlib.pyplot as plt
A=input("ENter 1st seqence:")
lenA=len(A)
AR=np.zeros(lenA)
rev=lenA-1
for x in xrange(0,lenA):
	AR[x]=A[rev]
	rev -=1

lenAR=len(AR)
C = np.zeros(lenA+ lenAR-1)    
for m in range(lenA):       
	for n in range(lenAR):
		C[m+n] = C[m+n] + A[m]*AR[n]
print(C)
a1=plt.subplot(311)
plt.stem(A)
plt.subplot(312,  sharex=a1, sharey=a1)
plt.stem(AR)
plt.subplot(313 , sharex=a1, sharey=a1)
plt.stem(C)
plt.show()