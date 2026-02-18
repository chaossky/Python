import numpy as np, matplotlib.pyplot as plt

x=np.linspace(-3,3,300)
y=np.linspace(-3,3,300)
X,Y=np.meshgrid(x,y)
Z=np.sin(X**2+Y**2)

plt.imshow(Z,cmap="coolwarm")
plt.colorbar(label="Emotion Intensity")
plt.axis("off")
plt.show()