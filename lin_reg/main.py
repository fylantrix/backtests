import numpy as np
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import random

class LinearRegression:
    def __init__(self) -> None:
        pass


plt.style.use("dark_background")

prices = {}

for ticker in ["GLD", "TLT"]:
    data = yf.Ticker(ticker).history(
        start="2025-01-01",
        end="2026-12-31",
        interval="1d",
        auto_adjust=True,
    )
    prices[ticker] = data["Close"]

returns_df = pd.DataFrame(prices).pct_change().dropna()


plt.figure(figsize=(8, 6))
plt.scatter(returns_df["GLD"], returns_df["TLT"], alpha=0.6)

plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.xlabel("GLD daily return")
plt.ylabel("TLT daily return")
plt.title("Daily Returns: GLD vs. TLT")
plt.grid(True, alpha=0.3)
ax = plt.gca()
ax.xaxis.set_major_formatter(PercentFormatter(1))
ax.yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
