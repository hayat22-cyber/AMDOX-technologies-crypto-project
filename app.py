
import streamlit as st
import pandas as pd
import plotly.express as px
from data import fetch_data
from models import run_arima, run_prophet
from risk import calculate_volatility, calculate_var, monte_carlo_simulation

st.set_page_config(page_title="CryptoVision AI", layout="wide")

st.title("🚀 CryptoVision AI - Cryptocurrency Forecasting & Risk Analytics System")

crypto = st.selectbox("Select Cryptocurrency", ["BTC-USD", "ETH-USD", "SOL-USD"])

df = fetch_data(crypto)

st.subheader("📈 Historical Price Trend")
fig = px.line(df, x="Date", y="Close")
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)

vol = calculate_volatility(df)
var_95 = calculate_var(df)
mc_price = monte_carlo_simulation(df)

col1.metric("Annualized Volatility", f"{vol:.2%}")
col2.metric("Value at Risk (95%)", f"{var_95:.2%}")
col3.metric("Monte Carlo Expected Price", f"${mc_price:.2f}")

st.subheader("🔮 Forecasting Models")

if st.button("Run ARIMA Forecast"):
    forecast = run_arima(df)
    st.line_chart(forecast)

if st.button("Run Prophet Forecast"):
    forecast = run_prophet(df)
    st.line_chart(forecast)
