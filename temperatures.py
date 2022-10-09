import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('WTG A.csv')
# sampleDF = df.sample(frac=1/20)
# sampleDF
sampleDF = df.head(20)
#st.write(df.columns)
fig = px.scatter(df, x ="Date & Time", y = "WTG-A (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 1 Temperature")
st.write(fig)

dfB = pd.read_csv('WTG B.csv')
sampleDFB = dfB.head(20)
#st.write(dfB.columns)
fig1 = px.scatter(dfB, x ="Date & Time", y = "WTG-B (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 2 Power")
st.write(fig1)

dfC = pd.read_csv('WTG C.csv')
sampleDFC = dfC.head(20)
#st.write(dfC.columns)
fig2 = px.scatter(dfC, x ="Date & Time", y = "WTG-C (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 3 Power")
st.write(fig2)

dfD = pd.read_csv('WTG D.csv')
sampleDFD = dfD.head(20)
#st.write(dfD.columns)
fig3 = px.scatter(dfD, x ="Date & Time", y = "WTG-D (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 4 Power")
st.write(fig3)

dfE = pd.read_csv('WTG E.csv')
sampleDFE = dfE.head(20)
#st.write(dfD.columns)
fig4 = px.scatter(dfE, x ="Date & Time", y = "WTG-E (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 5 Power")
st.write(fig4)

dfF = pd.read_csv('WTG F.csv')
sampleDFF = dfF.head(20)
#st.write(dfD.columns)
fig5 = px.scatter(dfF, x ="Date & Time", y = "WTG-F (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 6 Power")
st.write(fig5)

dfG = pd.read_csv('WTG G.csv')
sampleDFG = dfG.head(20)
#st.write(dfD.columns)
fig6 = px.scatter(dfG, x ="Date & Time", y = "WTG-G (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 7 Power")
st.write(fig6)

dfH = pd.read_csv('WTG H.csv')
sampleDFH = dfH.head(20)
#st.write(dfD.columns)
fig7 = px.scatter(dfH, x ="Date & Time", y = "WTG-H (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 8 Power")
st.write(fig7)

dfI = pd.read_csv('WTG I.csv')
sampleDFI = dfI.head(20)
#st.write(dfD.columns)
fig8 = px.scatter(dfI, x ="Date & Time", y = "WTG-I (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 9 Power")
st.write(fig8)

dfJ = pd.read_csv('WTG J.csv')
sampleDFJ = dfJ.head(20)
#st.write(dfD.columns)
fig9 = px.scatter(dfJ, x ="Date & Time", y = "WTG-J (2.82-FDR 2A) - HUB TEMPERATURE", opacity = .1, title = "Turbine 10 Power")
st.write(fig9)






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