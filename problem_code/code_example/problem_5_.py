from scipy.optimize import minimize
print(minimize(lambda x: ((10-x)**2 + (0-x**2-10)**2), 0., method='Nelder-Mead').x)
