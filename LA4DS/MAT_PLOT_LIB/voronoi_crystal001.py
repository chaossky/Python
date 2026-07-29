from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt

pts=np.random.rand(10,2)

vor=Voronoi(pts)
voronoi_plot_2d(vor)

plt.show()