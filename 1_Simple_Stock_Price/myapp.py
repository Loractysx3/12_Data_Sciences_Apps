import yfinance as yf
import pandas as pd
import streamlit as st

st.write('''
## Simple Stock Price App
         
Shown are the stock **closing price** and ***volume*** of Google !



''')

tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start = "2010-1-01", end = "2023-11-19")

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

