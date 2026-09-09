import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data for 3D Surface
X=np.linspace(-5,5,100)
Y=np.linspace(-5,5,100)
X,Y=np.meshgrid(X,Y)
Z=np.sin(np.sqrt(X**2+Y**2))

# Create 3D plot
Fig=plt.figure(figsize=(10,7))
ax=Fig.add_subplot(111,projection='3d')

surf=ax.plot_surface(X,Y,Z,cmap='viridis',edgecolor='none', alpha=0.9)

ax.set_title('3D Surface Plot - Sine Wave',fontsize=14)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

Fig.colorbar(surf,ax=ax,shrink=0.6,aspect=10)

plt.show()
