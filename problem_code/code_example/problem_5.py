from scipy.optimize import minimize
import numpy as np

def f(x):
    return x**2+10.

def dist(x):
    x_o, y_o = 10., 0.  #カメラマンの位置座標
    return np.sqrt((x-x_o)**2+(f(x)-y_o)**2)

sol = minimize(dist, 0., method='Nelder-Mead')
print(sol.x, f(sol.x))

#以下, プロットのためのコマンド
import matplotlib.pyplot as plt

x = np.linspace(0.,10, 100)
plt.xlim(0,12.5)
plt.ylim(0,12.5)
plt.plot(x, f(x))
plt.plot([10,sol.x],[0,f(sol.x)], linestyle='--')
plt.plot(sol.x, f(sol.x), marker='o',color='red')
plt.plot(10,0,marker='o',color='red')
plt.show()
