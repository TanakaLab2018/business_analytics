import matplotlib.pyplot as plt
import numpy as np

img = np.array([    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1] ])
plt.imshow(img, cmap='gray', interpolation='none')

plt.show()
