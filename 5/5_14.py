import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2)
plt.fill_between(x, np.sin(x), -np.sin(x), alpha=0.3)

plt.show()
