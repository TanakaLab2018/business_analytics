import numpy as np

a = np.array([[1, 2], [3, 4]])  #2次元の配列を生成
print('a =', a, '\n')

a.shape = (4,)  #1次元にフラットにする
print('a =', a, '\n')
