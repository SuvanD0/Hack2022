import pandas as pd
import streamlit as st


data = st.container()

max = st.container()



df = pd.read_csv('WTG A.csv')
df[df['WTG-A (2.82-FDR 2A) - POWER'].str.contains('Bad')==False]


with data:
    st.write(df.columns)
    st.write(df['WTG-A (2.82-FDR 2A) - POWER'].max())

