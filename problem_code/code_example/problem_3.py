from scipy.optimize import minimize
import numpy as np

def powell(x):
    return (x[0]-10.*x[1])**2 + 5.*(x[2]-x[3])**2 + (x[1]-2.*x[2])**4 + 10.*(x[0]-x[3])**4

x0 = [3., -1., 0., 1.]
res = minimize(powell, x0, method='Nelder-Mead')
print(res.x)

res = minimize(powell, x0, method='Powell')
print(res.x)
