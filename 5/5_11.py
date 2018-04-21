import matplotlib.pyplot as plt
import numpy as np

n = 11
plt.bar(np.arange(n), np.random.randint(100, 120, n), align='center', color='green')
plt.xticks(np.arange(n), [str(2010 + i) for i in range(n)])

plt.show()
