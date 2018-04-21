import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2)
y = np.sin(x)

plt.plot(x, y)
plt.show()  #jupiterの場合は必要ないが, プログラムを作る際にはこの表示する指示が必要
