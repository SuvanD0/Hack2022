import pandas as pd
import plotly.express as plt
import streamlit as st
df = pd.read_csv('WTG C.csv')
dfX=df.iloc[2:52562:144]
turbineCSample = dfX.iloc[:,[69]]
st.write(turbineCSample)
fig2 = plt.scatter(df, x ="Date & Time", y = "WTG-C (2.82-FDR 2A) - POWER", opacity = .1, title = "Turbine 3 Power")
st.write(fig2)
