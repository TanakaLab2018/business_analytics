import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

points = np.random.rand(9,2)
vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
plt.show()
print(vor.vertices)
print(vor.ridge_vertices)
print(vor.regions)
print(vor.point_region)
