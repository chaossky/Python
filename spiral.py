import matplotlib.pyplot as plt
import numpy as np

theta=np.linspace(0,8*np.pi,100)
r=theta**1.1

plt.polar(theta*0.7,r,color='magenta',linewidth=2)
plt.title("Spiral Plot")
plt.show()