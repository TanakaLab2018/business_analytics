import numpy as np

x = np.linspace(1, 3, 3)
y = np.linspace(-1, 3, 5)

print('x =', x, '\n')
print('y =', y, '\n')

X, Y = np.meshgrid(x, y)

print('X =', X, '\n')
print('Y =', Y, '\n')
