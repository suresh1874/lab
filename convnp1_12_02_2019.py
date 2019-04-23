import numpy as np
import matplotlib.pyplot as plt
A=input("ENter 1st seqence:")
B=input("ENter 2nd seqence:")
lengthA=len(A)  
lengthB=len(B)      
C = np.zeros(lengthA+ lengthB-1)    
for m in range(lengthA):       
	for n in range(lengthB):
		C[m+n] = C[m+n] + A[m]*B[n]

    	
print(C)

print("Convolve")
print(np.convolve(A,B))

a1=plt.subplot(311)

plt.stem(A)

plt.subplot(312,  sharex=a1, sharey=a1)

plt.stem(B)

plt.subplot(313 , sharex=a1, sharey=a1)

plt.stem(C)

plt.show()