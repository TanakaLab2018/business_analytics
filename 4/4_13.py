import numpy as np

x = np.array([1, 2, 3, 5])
v1 = np.vander(x)
print('v1 = \n', v1)

v2 = np.vander(x, increasing=True)
print('v2 = \n', v2)

v3 = np.vander(x, 2, increasing=True)
print('v3 = \n', v3)
