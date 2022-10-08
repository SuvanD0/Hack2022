import pandas as pd
import streamlit as st

data = st.container()

max = st.container()



df = pd.read_csv('WTG A.csv')
with data:
    st.write(df.columns)


with max:
    
    filtered = df(df[69]!='Bad')
    
    st.write(filtered[69].max())

