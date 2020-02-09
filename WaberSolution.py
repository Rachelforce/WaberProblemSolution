import numpy as np
from scipy.optimize import minimize
import math

x_ = np.array([3, 8, 1])  # X points coordinates
y_ = np.array([5, 2, 0])  # Y points coordinates
n = len(x_)  # points number


def length(x, a, b):  # length function for single point
    return math.sqrt(((a - x[0]) ** 2) + (b - x[1]) ** 2)


def fun(x):  # length function for all point
    f = 0
    for i in range(n):
        f += length(x, x_[i], y_[i])
    return f


x0 = np.array([3, 8])  # first point
res = minimize(fun, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})
print(res.x)
