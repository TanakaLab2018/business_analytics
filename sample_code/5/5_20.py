import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=100)
sns.set_style('dark')
sns.distplot(x)

plt.show()
