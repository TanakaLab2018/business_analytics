import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay, delaunay_plot_2d

np.random.seed(5)   #乱数の値を固定することが可能
points = np.random.rand(8, 2)
tri = Delaunay(points)
fig = delaunay_plot_2d(tri)
plt.show()
print(tri.simplices)
print(tri.neighbors)
