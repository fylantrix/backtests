import numpy as np
import matplotlib.pyplot as plt

T = 1.0
n_steps = 1_000
dt = T / n_steps

rng = np.random.default_rng(seed=42)
increments = rng.normal(loc=0.0, scale=np.sqrt(dt), size=n_steps)

time = np.linspace(0, T, n_steps + 1)
path = np.concatenate(([0.0], np.cumsum(increments)))

plt.plot(time, path)
plt.xlabel("Time")
plt.ylabel("W(t)")
plt.title("A Brownian Motion Path")
plt.grid(True)
plt.show()
