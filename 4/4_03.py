import numpy as np

a1 = np.array([0, 1, 2, 3])
print('a1 =', a1)
print('ndim:', a1.ndim)
print('shape:', a1.shape)
print('size:', a1.size)
print('\n')

a2 = np.array([[0, 1, 2, 3]])
print('a2 =', a2)
print('ndim:', a2.ndim)
print('shape:', a2.shape)
print('size:', a2.size)
print('\n')

a3 = np.array([[0], [1], [2], [3]])
print('a3 =', a3)
print('ndim:', a3.ndim)
print('shape:', a3.shape)
print('size:', a3.size)
print('\n')


#多分, 教科書にミスがあると思われます
#出力がa3のものになってしまっています
a4 = np.array([[[0]], [[1]], [[2]], [[3]]])
print('a4 =', a4)
print('ndim:', a4.ndim)
print('shape:', a4.shape)
print('size:', a4.size)
print('\n')
