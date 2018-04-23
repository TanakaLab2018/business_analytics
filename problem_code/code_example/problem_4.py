from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

#dataの中に[x座標, y座標, 人数]の順で情報を入力
data = np.array([    [24, 54, 2],
                    [60, 63, 1],
                    [1, 84, 2],
                    [23, 100, 3],
                    [84, 48, 4],
                    [15, 64, 5],
                    [52, 74, 4] ])

def f(x):
    return np.sum(np.array([data[i,2]*np.sqrt((data[i,0]-x[0])**2+(data[i,1]-x[1])**2) for i in range(len(data))]))

def sub(x):
    return  (50-x[0])**2 + (50-x[1])**2 - 40**2

con = {'type':'ineq', 'fun':sub}

res1 = minimize(f, (0,0), method='SLSQP')
res2 = minimize(f, (0,0), method='SLSQP', constraints=con)

print(res1.x)
print(res2.x)



#以下, プロットのためのコマンド (なので書く必要はなし)
for x in data:
    plt.plot(x[0], x[1], marker='*', color='blue')

plt.plot(res1.x[0],res1.x[1], marker='o', color='green')
plt.plot(res2.x[0],res2.x[1], marker='d', color='red')
plt.show()
