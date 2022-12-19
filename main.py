import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import plotly.express as px
import warnings 
import streamlit as st
warnings.filterwarnings("ignore") 
import seaborn as sns

from pandas_datareader import DataReader, data
from datetime import datetime

st.title('Stock EDA')
st.header('Target')
st.write('The target of this EDA is to draw conclusions about the relationship between different crypto stocks')

stock_name = st.text_input("Enter the stock name: \n")
option = st.slider("How many days of data would you like to see?", 1,60,1)


end = datetime.today().strftime('%Y-%m-%d')
start = (datetime.today() - timedelta(option)).strftime('%Y-%m-%d)
@st.cache
                                            
