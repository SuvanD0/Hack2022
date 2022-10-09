import sklearn
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('WTG A.csv')
st.write(df.shape)

clf = sklearn.svm.LinearSVC()