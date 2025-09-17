import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

points=np.random.rand(20,2)
vor=Voronoi(points)
voronoi_plot_2d(vor)
plt.plot(points[:,0],points[:,1],'ko')
plt.show()
