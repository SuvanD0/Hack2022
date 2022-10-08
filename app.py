import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/frankli/Desktop/OSU Hack Ohio Fall 2022 Data_Final.csv')
# sampleDF = df.sample(frac=1/20)
# sampleDF
sampleDF = df.head(20)
st.write(df.columns)
fig = px.scatter(df, x ="Date & Time", y = "WTG-A (2.82-FDR 2A) - POWER", opacity = .1)
st.write(fig)

dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - POWER", opacity = .1)
st.write(fig1)

dfB = pd.read_csv('WTG C.csv')
sampleDFB = dfB.head(20)
st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - POWER", opacity = .1)
st.write(fig1)


# import streamlit as st
# import pandas as pd

# header = st.container()
# dataset = st.container()
# features = st.container()
# modelTraining = st.container()

# with header:
#     st.title("AEP Wind Turbines")

# with dataset:
#     data = pd.read_csv('/Users/frankli/Desktop/OSU Hack Ohio Fall 2022 Data_Final.csv')
#     st.write(data.head())
#     st.write(list(data.columns))
#     power = pd.DataFrame(data["WTG-A (2.82-FDR 2A) - PRODUCTION"])
#     power.head()
#     # degreesC = pd.DataFrame(aepData[])
#     # st.button('Click me')
#     # st.text('frank')
#     # st.table(data.iloc[0,10])
#     #st.line_chart(data)


# with features:
#     st.header("Features")
# with modelTraining:
#     st.write("Model")