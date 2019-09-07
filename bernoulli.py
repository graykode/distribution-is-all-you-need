"""
    Code by Tae-Hwan Hung(@graykode)
    https://en.wikipedia.org/wiki/Bernoulli_distribution
"""
import random
import numpy as np
from matplotlib import pyplot as plt

def bernoulli(p, k):
    return p if k else 1 - p

n_experiment = 100
p = 0.6
x = np.arange(n_experiment)
y = []
for _ in range(n_experiment):
    pick = bernoulli(p, k=bool(random.getrandbits(1)))
    y.append(pick)

u, s = np.mean(y), np.std(y)
plt.scatter(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
plt.legend()
plt.savefig('graph/bernoulli.png')
plt.show()

