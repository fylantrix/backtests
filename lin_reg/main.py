import numpy as np
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import random

tickers = ["GLD", "TLT"]
class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs = 1000) -> None:
        self.w = 0
        self.b = 0
        self.learning_rate = learning_rate
        self.epochs = epochs
    def fit(self, x, y):
        n = len(x)
        for _ in range(self.epochs):
            # Predictions and errors
            predictions = [self.w * xi + self.b for xi in x]
            errors = [pred - yi for pred, yi in zip(predictions, y)]

            # Gradients of mean squared error
            dw = (2 / n) * sum(xi * err for xi, err in zip(x, errors))
            db = (2 / n) * sum(errors)

            # Update parameters
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, x):
        return [self.w * xi + self.b for xi in x]


plt.style.use("dark_background")

prices = {}

for ticker in tickers:
    data = yf.Ticker(ticker).history(
        start="2026-01-01",
        end="2026-12-31",
        interval="1d",
        auto_adjust=True,
    )
    prices[ticker] = data["Close"]

returns_df = pd.DataFrame(prices).pct_change(periods=10).dropna()

x = returns_df["GLD"].to_numpy() * 100
y = returns_df["TLT"].to_numpy() * 100

lr = LinearRegression()
lr.fit(x, y)

# Build a line across the observed GLD returns
x_line = np.linspace(x.min(), x.max(), 200)
y_line = np.array(lr.predict(x_line)) / 100  # back to decimal returns

plt.figure(figsize=(8, 6))
plt.scatter(returns_df["GLD"], returns_df["TLT"], alpha=0.6, label="Observed returns")
plt.plot(x_line / 100, y_line, color="orange", linewidth=2, label="Regression line")

plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.xlabel("GLD 10-trading-day return")
plt.ylabel("TLT 10-trading-day return")
plt.title("GLD vs. TLT Returns with Linear Regression")
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

print(f"Slope: {lr.w:.3f}")
print(f"Intercept: {lr.b:.3f}%")
