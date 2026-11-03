import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import mplfinance as mpf

plt.style.use("dark_background")

tickers = ["GLD", "TLT"]

fig, axes = plt.subplots(
    nrows=2,
    ncols=1,
    figsize=(12, 8),
    sharex=True,
)

for ticker, ax in zip(tickers, axes):
    data = yf.Ticker(ticker).history(
        start="2025-01-01",
        end="2026-12-31",
        interval="1d",
        auto_adjust=True,
    )

    mpf.plot(
        data,
        type="candle",
        ax=ax,
        style="yahoo",
        show_nontrading=False,
        mav=20,
    )
    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.5)
    ax.grid(axis="x", linestyle="--", linewidth=0.6, alpha=0.5)
    ax.set_title(ticker)

fig.tight_layout()
plt.show()

