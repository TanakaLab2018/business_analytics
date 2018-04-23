from scipy.optimize import minimize

print(minimize(lambda x: ((10-x)**2 + (0-x**2-10)**2), 0., method='SLSQP').x)


#以下, プロットのためのコマンド
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
def f(x):
    return x**2+10.
sol = minimize(lambda x: ((10-x)**2 + (0-x**2-10)**2), 0., method='SLSQP').x
plt.xlim(0,12.5)
plt.ylim(0,12.5)
plt.plot(x, f(x))
plt.plot(10,0,marker='o')
plt.plot(sol, f(sol), marker='o')
plt.plot([10,sol],[0,f(sol)], linestyle='--')
plt.show()
