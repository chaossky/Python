# 3d_plot001.py
# 3D bar plot with no tick labels
# Source: https://matplotlib.org/stable/gallery/mplot3d/bar3d.html
import matplotlib.pyplot as plt
import numpy as np

# Set the style
# Uncomment the next line to use a specific style       
plt.style.use('_mpl-gallery')

# Make data
x = [1, 1, 2, 3]
y = [1, 2, 1, 2]
z = [0, 0, 0, 0]
# Define the width, depth, and height of the bars
dx = np.ones_like(x)*0.5 # Width of the bars
#np.ones_like returns an array of ones with the same shape as x
dy = np.ones_like(x)*0.5
dz = [2, 3, 1, 4]

# Plot
# Create a 3D subplot 
# the subplot is defined with a projection of '3d'
# fig is the figure object and ax is the axes object
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.bar3d(x, y, z, dx, dy, dz)

# Set the title
ax.set_title('3D Bar Plot with No Tick Labels')
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

# Show the plot
plt.tight_layout()   
plt.show()