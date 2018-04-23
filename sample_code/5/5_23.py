import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

g = sns.FacetGrid(row='sex', col='time', hue='smoker', hue_kws={'marker':['x', 'o']}, data=tips)
g.map(sns.regplot, 'total_bill', 'tip')

plt.show()
