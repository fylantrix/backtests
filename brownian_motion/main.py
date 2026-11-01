import numpy as np
import matplotlib.pyplot as plt
import random

T = 1.0
N_STEPS = 5000
N_SIMS = 5000
dt = T / N_STEPS

rng = np.random.default_rng(seed=random.randrange(1, 2000))
increments = rng.normal(
    loc=0.0,
    scale=np.sqrt(dt),
    size=(N_SIMS, N_STEPS)
)
path = np.concatenate(
    [np.zeros((N_SIMS, 1)), np.cumsum(increments, axis=1)],
    axis=1
)

endpoints = path[:, -1]
running_mean_end = np.cumsum(endpoints) / np.arange(1, N_SIMS + 1)

time = np.linspace(0, T, N_STEPS + 1)
mean_path = np.mean(path, axis=0)

fig, axs = plt.subplots(2, 1, figsize=(9, 8))

axs[0].plot(np.arange(1, N_SIMS + 1), running_mean_end)
axs[0].set_xscale("log")
axs[0].axhline(0, color="gray", linestyle="--")
axs[0].set_xlabel("Number of paths")
axs[0].set_ylabel("Running average endpoint")
axs[0].set_title("Average Endpoint as More Paths Are Included")
axs[0].grid(True)

axs[1].plot(time, mean_path)
axs[1].axhline(0, color="gray", linestyle="--")
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Mean W(t)")
axs[1].set_title("Mean Path")
axs[1].grid(True)

plt.tight_layout()
plt.show()
