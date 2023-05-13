import pandas as pd
import streamlit as st

df = pd.read_excel('2023_04_27.xlsx',engine='openpyxl')
st.table(df)
