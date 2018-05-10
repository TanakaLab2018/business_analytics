import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np, pandas as pd, matplotlib.pyplot as plt

n = 20
x1 = np.linspace(1, n-1, n)
y = 3.14*x1 + 1e-6 * np.random.random(n)

plt.plot(x1, y, '.')
plt.xlabel('x1')
plt.ylabel('y')
plt.xlim((0, x1.max()+1))

plt.show()
