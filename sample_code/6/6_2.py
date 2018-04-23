from scipy.optimize import rosen
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-1.5, 2., 100)
y = np.linspace(-0.5, 3., 100)

X, Y = np.meshgrid(x, y)
Z = rosen((X, Y))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)

plt.show()
