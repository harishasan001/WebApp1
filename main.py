import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from pandas_datareader import DataReader
from datetime import datetime

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
