import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('turbinefinalnobad2.csv')
df = df.drop(df.columns[0], axis=1)



# sampleDF = df.sample(frac=1/20)
# sampleDF
sampleDF = df.head(20)




# fig1 = px.scatter(df,x= "turbine" ,y = 'blade1actual', opacity = .5, title = "Turbine 2 - BLADE 1 - SET VALUE")
# st.write(fig1)
xChoice = st.selectbox('X-Axis',df.columns)
yChoice = st.selectbox('Y-Axis',df.columns)
fig1 = px.scatter(df,y= yChoice ,x = xChoice ,color='turbine', opacity = .5, title = "Turbine Data Values")
fig1.update_layout(autotypenumbers='convert types')

st.write(fig1)
col1,col2,col3 = st.columns([1,4,1])
col2.write("Press turbine icons on right side of graph to view specific turbines!")

fig2 = px.line(df, x=xChoice, y = yChoice, color = 'turbine', title = "Power vs Turbine")
fig2.update_layout(autotypenumbers='convert types')
st.write(fig2)


