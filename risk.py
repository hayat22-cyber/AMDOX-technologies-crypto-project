
import numpy as np

def calculate_volatility(df):
    returns = df['Close'].pct_change().dropna()
    return np.std(returns) * np.sqrt(252)

def calculate_var(df, confidence=0.95):
    returns = df['Close'].pct_change().dropna()
    return np.percentile(returns, (1-confidence)*100)

def monte_carlo_simulation(df, simulations=1000, days=30):
    returns = df['Close'].pct_change().dropna()
    last_price = df['Close'].iloc[-1]
    mean = returns.mean()
    std = returns.std()

    prices = []
    for _ in range(simulations):
        price = last_price
        for _ in range(days):
            price *= (1 + np.random.normal(mean, std))
        prices.append(price)

    return np.mean(prices)
