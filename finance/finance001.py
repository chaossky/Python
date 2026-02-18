import yfinance as yf
import pandas as pd

stock=yf.Ticker("005930.KQ")
data=stock.history(period="1y")

data.head()