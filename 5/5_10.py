import matplotlib.pyplot as plt
import numpy as np

plt.hist(np.random.randn(100000) * 10 + 50, bins=60, range=(20, 80))

plt.show()
