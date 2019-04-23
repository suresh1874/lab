import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal


def showCircularConvolution(n0):
    n = np.arange(N)
    plt.subplot(211)
    plt.plot(n, x[n], label='$x[n]$')
    plt.plot(n, h[(n0-n)%N], label='$h[(n_0-n)_N]$')
    plt.plot(n, x[n] * h[(n0-n)%N], label=r'$x[n]\cdot h[(n_0-n)_N]$')
    
    plt.subplot(212)
    hx = np.fft.ifft(np.fft.fft(x[n]) * np.fft.fft(h[n])) # use convolution theorem
    plt.plot(n, abs(hx[n]))
    current = sum(x[np] * h[(n0-np) % N] for np in n)     # direct calculation for the convolution
    plt.plot(n0, current, 'ro')
    plt.show()



N = 128   # the sequence length
# Generate some random sequence we use for the convolution
x = abs(N*np.fft.ifft(np.random.randn(5)+1j*np.random.randn(5), N))
# use some exponential sequence for the second function
h = np.exp(-0.1*np.arange(N))


showCircularConvolution(50)
plt.plot(x, label='$x[n]$');
plt.plot(h, label='$h[n]$');
plt.show()