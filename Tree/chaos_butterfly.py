import numpy as np,matplotlib.pyplot as plt

x=y=z=0.01
dt=0.01;xs=[];ys=[]

for _ in range(10000):
    dx=10*(y-x)
    dy=x*(20-z)-y
    dz=x*y-8/3*z
    x+=dx*dt;y+=dy*dt;z+=dz*dt
    xs.append(x); ys.append(y)

plt.plot(xs,ys,linewidth=0.5)
plt.axis("off")
plt.show()