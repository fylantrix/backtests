import numpy as np
import matplotlib.pyplot as plt
import random

N_SIMS = 100

np.random.seed(random.randint(1, 1000000))
data = {'a': np.arange(N_SIMS),
        'c': np.empty(1)
        }
data['b'] = data['a'] + 10 * np.random.randn(N_SIMS)
# data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()
