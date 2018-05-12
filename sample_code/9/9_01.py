import numpy as np
import scipy.linalg as linalg
from sklearn.datasets import *
import matplotlib.pyplot as plt
import sklearn.svm as svm

np.random.seed(0)
X, Y = make_classification(n_features=2, n_redundant=0, n_informative=2)
iy = (Y==1)
iny = (Y==0)
plt.scatter(X[iy, 0], X[iy, 1], marker='o')
plt.scatter(X[iny, 0], X[iny, 1], marker='x')
plt.show()
plt.close()

clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X, Y)

xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])    #ravelのあとに()が必要
Z = Z.reshape(xx.shape)

ctr = plt.contour(xx, yy, z, levels=[0], linetypes='--')
plt.scatter(X[iy, 0], X[iy, 1], marker='o')
plt.scatter(X[iny, 0], X[iny, 1], marker='x')
plt.axis([xx.min(), xx.max(), yy.min(), yy.max()])

plt.show()
