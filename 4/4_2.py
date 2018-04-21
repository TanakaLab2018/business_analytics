import numpy as np

a = np.array([1, 2, 3, 4.0])
print('a =', a, '\n')

b = np.array([[1, 2, 3], [4, 5.0]])
print('b =', b, '\n')

c = np.array([[1], [2], [3], [4]])
print('c =', c, '\n')

d = np.array([[1, 2, 3], [4, 5, 6], (7, 8, 9.0)])
print('d =', d, '\n')

e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]])
print('e =', e, '\n')

f = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
print('f =', f, '\n')
