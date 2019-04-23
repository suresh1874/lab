import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10*np.pi,0.1)
y = 5*(np.sin(x))
plt.plot(x,y)
plt.show()
