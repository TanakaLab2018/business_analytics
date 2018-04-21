import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(np.random.rand(100), np.random.rand(100), np.random.rand(100))

plt.show()
