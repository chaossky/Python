import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def f(x):
   return x**2+10*np.sin(x/8)

x=np.arange(-10,10,0.1)
plt.plot(x,f(x))
plt.show()

