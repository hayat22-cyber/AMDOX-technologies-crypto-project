
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
import pandas as pd

def run_arima(df):
    model = ARIMA(df['Close'], order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=30)
    return forecast

def run_prophet(df):
    prophet_df = df[['Date','Close']].rename(columns={'Date':'ds','Close':'y'})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast[['ds','yhat']].set_index('ds')
