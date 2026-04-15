import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A=np.array([[-2,3],[2,8]])
vi=np.linspace(-2,2,30)
qf=np.zeros((len(vi),len(vi)))

X,Y=np.meshgrid(vi,vi)

for i in range(len(vi)):
    for j in range(len(vi)):
        v=np.array([vi[i],vi[j]])
        qf[i,j]=v.T@A@v/(v.T@v)
        
# ax=plt.axes(projection='3d')
ax=plt.figure().add_subplot(projection='3d')
ax.plot_surface(X,Y,qf.T)
ax.set_xlabel(r'$ v_1 $'),ax.set_ylabel(r'$ v_2 $')
ax.set_zlabel(r'$ \zeta $')

plt.show()
        
        