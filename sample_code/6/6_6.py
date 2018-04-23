import numpy as np
from scipy.optimize import brentq, root

def f(x):
    return x**2 - 4. * np.sin(x)

print(brentq(f, 1.0, 3.0), '\n')

print(root(f, 2.0), '\n')
