import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2)

plt.title('Sin curve')
plt.plot(x, np.sin(x), c='navy', marker='*', label='sin')
plt.plot(x, np.sin(-x), c='#9400D3', linestyle='--', label='-sin')
plt.plot(x, np.cos(x), c=(1.0, 0.5, 0.0), label='cos')
plt.xlabel('x value')
plt.ylabel('y value', size=15)
plt.xlim((0, 2 * np.pi))
plt.xticks(np.linspace(0, 2 * np.pi, 5), ['0', 'pi/2', 'pi', '3 pi/2', '2pi'])
plt.legend(loc='upper right', shadow=True)

plt.show()
