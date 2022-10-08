import pandas as pd
import streamlit as st

df = pd.read_csv('WTG A.csv')
st.write(df.columns)