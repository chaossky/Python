import matplotlib.pyplot as plt, numpy as np
theta=np.linspace(0,16*np.pi,1000)
r=np.linspace(0,1,1000)
colors=theta
plt.figure(figsize=(6,6))
plt.subplot(projection='polar')
plt.scatter(theta,r,c=colors,cmap='hsv',s=10)
plt.show()