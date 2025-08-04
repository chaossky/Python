import numpy as np
import matplotlib.pyplot as plt

a=np.array([1, 2]) #1D array, vector
b=np.array([3, 4]) #1D array, vector

c=a+b

plt.arrow(0, 0, a[0], a[1], head_width=0.1, head_length=0.2, fc='blue', ec='blue', label='a')
plt.arrow(0, 0, b[0], b[1], head_width=0.1, head_length=0.2, fc='red', ec='red', label='b')
v= np.array([1, 2, 3,4,5,6,7])
v_dim=len(v)#mathematical dimension of v

v_mag=np.linalg.norm(v)
#mathematical magnitude of v,length, norm

print("v=",v)
print("v_dim=",v_dim)
print("v_mag=",v_mag)