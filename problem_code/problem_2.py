from scipy.optimize import minimize
import numpy as np

def beale(x):
    c = np.array([0, 1.5, 2.25, 2.625])
    return np.sum([(c[i] - x[0]*(1. - (x[1])**i))**2  for i in range(1,4)])

x0 = [1.,0.8]
res = minimize(beale, x0, method='Nelder-Mead')
print(res.x)
