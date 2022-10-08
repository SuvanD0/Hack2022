import pandas as pd
import streamlit as st

df = pd.read_csv('WTG A.csv')

faults= df['WTG-A (2.82-FDR 2A) - STATE AND FAULT'].contains('Fault').inde
