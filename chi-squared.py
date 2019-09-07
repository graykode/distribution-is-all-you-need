"""
    Code by Tae-Hwan Hung(@graykode)
    https://en.wikipedia.org/wiki/Chi-squared_distribution
"""
import numpy as np
from matplotlib import pyplot as plt

def gamma_function(n):
    cal = 1
    for i in range(2, n):
        cal *= i
    return cal

def chi_squared(x, k):

    c = 1 / (2 ** (k/2)) * gamma_function(k//2)
    y = c * (x ** (k/2 - 1)) * np.exp(-x /2)

    return x, y, np.mean(y), np.std(y)

for k in [2, 3, 4, 6]:
    x = np.arange(0, 10, 0.01, dtype=np.float)
    x, y, _, _ = chi_squared(x, k)
    plt.plot(x, y, label=r'$k=%d$' % (k))

plt.legend()
plt.savefig('graph/chi-squared.png')
plt.show()
