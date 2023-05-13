import pandas as pd
import streamlit as st

df = pd.read_csv('부산광역시_법정동별연료별차종별_자동차등록대수_20230331.csv')

st.table(df)
