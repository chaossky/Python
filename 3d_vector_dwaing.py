import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origin of the vector
origin = [0, 0, 0]

# Components of the vector
vector1 = [2, 3, 4]
vector2 = [1, 1, 1]

# Plot the vector using quiver
ax.quiver(*origin, *vector1, color='r', arrow_length_ratio=0.1)
ax.quiver(*origin, *vector2, color='b', arrow_length_ratio=0.1)

# Set axes limits
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title("3D Vector using Matplotlib")
plt.show()
