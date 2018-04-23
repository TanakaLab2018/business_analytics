from scipy.spatial import KDTree
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

points = np.random.rand(10000,2)
tree = KDTree(points,10)
ball = tree.query_ball_point([0.5, 0.5], 0.1)   #(0.5,0.5)から距離0.1の点を抽出
plt.plot(points[:,0], points[:,1], 'b+')
plt.plot(points[ball,0], points[ball,1], 'ro')
plt.show()
