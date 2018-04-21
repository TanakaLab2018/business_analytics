import numpy as np

a = np.arange(1, 13).reshape((4,3))
b = np.diag([1, 2, 3, 4])
c = np.diag(a)
d = np.tri(3)
e = np.tri(4,5)

print('a =', a, '\n')   #aも出力しました
print('b =', b, '\n')
print('c =', c, '\n')
print('d =', d, '\n')
print('e =', e, '\n')
