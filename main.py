import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import plotly.express as px
import warnings 
import streamlit as st
warnings.filterwarnings("ignore") 
import seaborn as sns

from pandas_datareader import DataReader, data
from datetime import datetime, timedelta
import yfinance as yf

st.title('Stock EDA')
st.subheader('Target')
st.write('The target of this EDA is to explore a particular stock data in detail')

stock = st.text_input("Enter the stock name: \n")
option = st.slider("How many days of data would you like to see?", 1,365,1)

end = datetime.today().strftime('%Y-%m-%d')
start = (datetime.today() - timedelta(option)).strftime('%Y-%m-%d')

get_stock_data = yf.Ticker(stock)

# Set the time line of your data
ticket_df = get_stock_data.history(period='1d', start=start, end=end)

st.subheader('Closing Price')
st.line_chart(ticket_df.Close)

st.subheader('Volume')
st.line_chart(ticket_df.Volume)
