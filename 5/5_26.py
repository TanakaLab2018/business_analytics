import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.factorplot(x='class', y='survived', col='sex', data=titanic)

plt.show()
