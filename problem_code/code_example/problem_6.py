from scipy.optimize import minimize
import numpy as np

def dist(x):
    return np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)

def sub(x):
    return 2.*x[0]**2 + x[1]**2 + x[2]**2 - 1000

con = {'type':'eq', 'fun':sub}

res = minimize(dist, (10,10,10), method='SLSQP', constraints=con)
print(res.x)
