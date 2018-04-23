import numpy as np

def print_data(T):
    print('ndim:', T.ndim)
    print('shape:', T.shape)
    print('size:', T.size)
    print('\n')


a1 = np.array([0, 1, 2, 3])
print('a1 =', a1)
print_data(a1)

a2 = np.array([[0, 1, 2, 3]])
print('a2 =', a2)
print_data(a2)

a3 = np.array([[0], [1], [2], [3]])
print('a3 =', a3)
print_data(a3)

a4 = np.array([[[0]], [[1]], [[2]], [[3]]])
print('a4 =', a4)
print_data(a4)
