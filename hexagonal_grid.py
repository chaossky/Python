import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

n=10
for i in range(n):
    for j in range(n):
        x=i+0.5*(j%2)
        y=np.sqrt(3)/2*j
        plt.scatter(x,y,c=np.random.rand(3,),s=500,marker='h')
    
plt.axis('equal')
plt.axis('off')
plt.show()