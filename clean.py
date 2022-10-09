import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('WTG A.csv')
df1 = df.iloc[:, [1, 11, 12, 13, 14, 15, 16, 69, 83, 87, 90, 96, 127]].copy()
# df
# df1
df1.fillna(0)
#df2 = df1.sort_values(by=['WTG-A (2.82-FDR 2A) - POWER'],ascending=False)
fig = px.scatter(df1, x ="Date & Time", y = "WTG-A (2.82-FDR 2A) - POWER", opacity = .1, title = "Turbine 1 Power", )
st.write(fig)