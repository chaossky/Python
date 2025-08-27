import numpy as np
import matplotlib.pyplot as plt

seed=90000
x=np.random.rand(seed)
y=np.random.rand(seed)
colors=np.random.rand(seed)

plt.scatter(x,y,c=colors, cmap='rainbow',s=30)
plt.axis(
    'off'
)
plt.show()