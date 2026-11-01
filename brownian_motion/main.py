import numpy as np
import matplotlib.pyplot as plt
import random

T = 1.0
N_STEPS = 1000
N_SIMS = 2000
dt = T / N_STEPS

path = np.empty((N_SIMS,N_STEPS + 1))

for i in range(N_SIMS):
    rng = np.random.default_rng(seed=random.randrange(1, 2000))
    increments = rng.normal(loc=0.0, scale=np.sqrt(dt), size=N_STEPS)
    gen = np.concatenate(([0.0], np.cumsum(increments)))
    path[i] = gen

time = np.linspace(0, T, N_STEPS + 1)
mean_end = np.mean(path[:, -1], axis=0)
mean_path = np.mean(path, axis=0)


print(mean_end)

plt.plot(time, mean_path.T)
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.title("Brownian Motion Average Path")
plt.grid(True)
plt.show()
