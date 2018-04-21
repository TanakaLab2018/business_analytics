import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2)
y = np.sin(x)

plt.subplot(131)
plt.plot(x, y, 'ro')

plt.subplot(132)
plt.plot(x, y, 'gD-')

plt.subplot(133)
plt.plot(x, np.sin(x), c='navy', marker='*')
plt.plot(x, np.sin(-x), c='#9400D3', linestyle='--')
plt.plot(x, np.cos(x), c=(1.0, 0.0, 0.0))

plt.show()
