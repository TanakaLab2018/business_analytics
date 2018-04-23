from scipy.optimize import curve_fit
import numpy as np

def f(x, a, b, c):
    return a*x**2 + b*x + c

xdata = np.linspace(-10, 10, 20)
ydata = f(xdata, 1, 1, 1) + np.random.normal(size=len(xdata))
param, cov = curve_fit(f, xdata, ydata)
print(param)
