import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import plotly.express as px
import warnings 
import streamlit as st
warnings.filterwarnings("ignore") 
import seaborn as sns

from pandas_datareader import DataReader
from datetime import datetime

st.title('Crypto Stock EDA')
st.header('Target')
st.write('The target of this EDA is to draw conclusions about the relationship between different crypto stocks')


tech_list = ['COIN','MSTR','NVDA','MARA', 'SQ', 'SI', 'RIOT', 'AMD', 'PYPL', 'CME']

#Setting the end date to today
end = datetime.now()

#Start date set to 2 year back
start = datetime(end.year-2,end.month,end.day)

#Using Yahoo Finance to grab the stock data
for stock in tech_list:
    globals()[stock] = DataReader(stock,'yahoo',start,end)
    
#testing if the global variable worked 
st.dataframe(COIN.head())
