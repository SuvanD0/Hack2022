import joblib
import pandas as pd
import streamlit as st

joblib.load('model.sav')

data = st.file_uploader("Upload a CSV file")

st.write(data)
