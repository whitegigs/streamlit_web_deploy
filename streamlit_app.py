import pandas as pd
import streamlit as st

df = pd.read_excel('streamlit_web_deploy/2023_04_27.xlsx')
st.table(df)
