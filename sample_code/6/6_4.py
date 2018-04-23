from scipy.optimize import minimize

f = lambda x: -x[0]-x[1]

'''  次のように書いても大丈夫です
def f(x):
    return -x[0]-x[1]
'''

con = {'type': 'ineq', 'fun':lambda x: -x[0]**2 - x[1]**2 + 2.}

''' 次のように関数を定義して記述しても大丈夫です
def f2(x):
    return -x[0]**2 - x[1]**2 + 2.
con = {'type': 'ineq', 'fun':f2}
'''

res = minimize(f, (2., 2.), method='SLSQP', constraints=con)
print(res.x)
