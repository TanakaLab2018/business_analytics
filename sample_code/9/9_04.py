import matplotlib.pyplot as plt
import numpy as np
import sklearn.svm as svm

np.random.seed(1000)
n = 1000
x = np.sort(np.random.uniform(-np.pi,np.pi,n))
y = np.sin(x) + np.random.randn(n)*0.2

svr_rbf = svm.SVR(kernel='rbf', C=1000, gamma=0.1)

x = x.reshape(-1,1)
y = y.reshape(-1,1)

y_rbf = svr_rbf.fit(x, y).predict(x)

plt.scatter(x, y, c='k', label='data', marker = '.')
plt.plot(x, y_rbf, c='r', label='RBF model', lw = 3)
plt.plot(x, np.sin(x), c='g', lw = 3 , linestyle='--')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend(loc='upper center', bbox_to_anchor=(1.4,0.7))
plt.show()
