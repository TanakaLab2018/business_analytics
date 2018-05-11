import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np, pandas as pd, matplotlib.pyplot as plt

a = pd.read_csv('./spam.csv')
a = sm.spam
a[a.spam == 0].numwords.hist(bins=3, label='not spam', alpha=0.5)
a[a.spam == 1].numwords.hist(bins=6, label='spam', alpha=0.5)
plt.xlabel('numwords')
plt.ylabel('number of cases')
plt.legend()

plt.show()
