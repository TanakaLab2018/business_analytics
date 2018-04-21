import numpy as np

z1 = np.zeros(3,)
print('z1 =', z1, '\n')

z2 = np.zeros((2,3))
print('z2 =', z2, '\n')

L = [[1.0, 2, 3], [4, 5, 6], [7, 8, 9]] #これはlistで, ndarrayではないことに注意
z3 = np.zeros_like(L, dtype=int)
print('z3 =', z3, '\n')
