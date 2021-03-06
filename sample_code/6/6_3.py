from scipy.optimize import minimize, rosen, rosen_der, rosen_hess


x0 = [2.0 for i in range(5)]

res = minimize(rosen, x0, method='Nelder-Mead')
print(res.x, '\n')

res = minimize(rosen, x0, jac=rosen_der, method='BFGS')
print(res.x, '\n')

res = minimize(rosen, x0, jac=rosen_der, hess=rosen_hess, method='trust-ncg')
print(res.x, '\n')
