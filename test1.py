import streamlit as st
import pandas as pd
import numpy as np

st.title("my sexy little")


date_column="date/time"

@st.cache #to increase speed of app (decorator)
def get data():
  data=pd.read_csv
  
  
data=get_data()
