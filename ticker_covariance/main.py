import numpy as np
import warnings
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

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
print(returns_df.head(2))
cov_matrix = returns_df.cov()

print(cov_matrix)
fig, ax = plt.subplots()
window = 30

rolling_cov = (
    returns_df["GLD"]
    .rolling(window)
    .cov(returns_df["TLT"])
)

rolling_cov.plot(title=f"GLD–TLT Rolling Covariance ({window} trading days)")
plt.ylabel("Covariance")
plt.show()

