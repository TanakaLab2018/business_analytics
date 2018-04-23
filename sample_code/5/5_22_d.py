import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.jointplot(x='tip', y='total_bill', data=tips, kind='hex')

plt.show()
