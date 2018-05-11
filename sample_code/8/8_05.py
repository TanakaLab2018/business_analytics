import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np, pandas as pd, matplotlib.pyplot as plt

n = 20
x1 = np.linspace(1, n-1, n)
y = 3.14*x1 + 1e-6 * np.random.random(n)

model1 = sm.OLS(y, x1)
model2 = sm.GLM(y, x1)
model3 = smf.glm('y ~ x1 -1',{'y':y,'x1':x1})
r1 = model1.fit()
r2 = model2.fit()
r3 = model3.fit()

for i, r in enumerate([r1, r2, r3]):
    plt.subplot(1, 3, i+1)
    plt.plot(x1, y, '.')
    if i < 2:
        plt.plot(x1, r.predict(x1))
    else:
        plt.plot(x1, r.predict({'x1':x1}))

    plt.title(['OLS', 'GLM', 'glm'][i])
    plt.xlabel('x1')
    plt.ylabel('y')
    plt.xlim((0, x1.max()+1))
    plt.ylim((0, y.max()+5))

plt.show()
