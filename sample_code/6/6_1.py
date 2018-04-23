from scipy.optimize import minimize_scalar

def f(x):
    return x/(1+x**2)

print(minimize_scalar(f, method='Brent'), '\n')
print(minimize_scalar(f, method='Golden'), '\n')
print(minimize_scalar(f, bounds=(-2,0), method='Bounded'), '\n')
