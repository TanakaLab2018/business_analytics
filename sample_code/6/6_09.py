import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d

points = np.random.rand(8,2)
print(points)
hull = ConvexHull(points)
fig = convex_hull_plot_2d(hull)
plt.show()
print(hull.vertices)
print(hull.simplices)
print(hull.neighbors)
