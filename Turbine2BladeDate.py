import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('WTG A.csv')


# sampleDF = df.sample(frac=1/20)
# sampleDF
sampleDF = df.head(20)


df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].isna().sum()
dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - BLADE 1 - ACTUAL VALUE", opacity = .1, title = "Turbine 2 - BLADE 1 - SET VALUE")
st.write(fig1)

df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].isna().sum()
dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - BLADE 1 - SET VALUE", opacity = .1, title = "Turbine 2 - BLADE 1 - SET VALUE")
st.write(fig1)


df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].isna().sum()
dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - BLADE 2 - ACTUAL VALUE", opacity = .1, title = "Turbine 2 - BLADE 1 - SET VALUE")
st.write(fig1)

df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].isna().sum()
dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - BLADE 2 - SET VALUE", opacity = .1, title = "Turbine 2 - BLADE 1 - SET VALUE")
st.write(fig1)

df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].isna().sum()
dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - BLADE 3 - ACTUAL VALUE", opacity = .1, title = "Turbine 2 - BLADE 1 - SET VALUE")
st.write(fig1)

df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].isna().sum()
dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - BLADE 3 - SET VALUE", opacity = .1, title = "Turbine 2 - BLADE 1 - SET VALUE")
st.write(fig1)