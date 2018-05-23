import matplotlib.pyplot as plt
import numpy as np
import sklearn.svm as svm

np.random.seed(100)
n = 50
x = np.sort(np.random.uniform(-np.pi,np.pi,n))
y = np.sin(x) + np.random.randn(n)*0.3

svr_rbf = svm.SVR(kernel='rbf', C=1000, gamma=0.1)
svr_lin = svm.SVR(kernel='linear', C=1000)
svr_poly = svm.SVR(kernel='poly', C=1000, degree=3)

x = x.reshape(-1,1)
y = y.reshape(-1,1)

y_rbf = svr_rbf.fit(x, y).predict(x)
y_lin = svr_lin.fit(x, y).predict(x)
y_poly = svr_poly.fit(x, y).predict(x)

plt.scatter(x, y, c='k', label='data')
plt.plot(x, y_rbf, c='g', label='RBF model')
plt.plot(x, y_lin, c='r', label='Linear model', linestyle='--')
plt.plot(x, y_poly, c='b', label='Polynomial model',linestyle=':')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend(loc='upper center', bbox_to_anchor=(1.4,0.7))
plt.show()
