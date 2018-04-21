import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.lmplot(x='fare', y='survived', col='sex', data=titanic, logistic=True)

plt.show()
