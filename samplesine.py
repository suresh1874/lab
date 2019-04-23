import matplotlib.pyplot as plt
import numpy as np
Fs = 800
f = 10
sample = 1000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
print(len(y))
result=[]
sumres=0x
for k in range(sample):	
	for m in range(k):
		sumres=sumres+(y[m])
	result.append(sumres)
plt.subplot(3,1,1)
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.subplot(3,1,2)
plt.stem(x,y, 'r', )
plt.subplot(3,1,3)
plt.stem(x,result)
plt.show()