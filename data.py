
import yfinance as yf
import pandas as pd

def fetch_data(symbol):
    df = yf.download(symbol, period="2y", interval="1d")
    df.reset_index(inplace=True)
    return df
