import numpy as np
import matplotlib.pyplot as plt
import math
import cmath as cm
w=np.arange(0,np.pi*2*10000,10)
dp=0.8
ds=0.2
wp=2*np.pi*4000
ws=2*np.pi*5000

#dp=np.float(input("Enter Pass Band Gain dp:"))
#ds=np.float(input("Enter Stop Band Gain ds:"))
#wp=np.float(input("Enter Pass Band cuttof freq :"))
#ws=np.float(input("Enter Stop Band cuttof freq:"))

def butter(dp,ds,wp,ws):
	a=(1/(dp**2))-1
	b=(1/(ds**2))-1
	N=int(np.ceil(0.5*np.log10(a/b)/np.log10(wp/ws)))
	wc=wp/(a**(1/2*N))

	return float(N),float(wc);

N,wc=butter(dp,ds,wp,ws)

print(N,wc)

BMag=np.abs(1/((1+(w/wc)**(2*N))**0.5))

plt.plot(w,BMag)
plt.show()