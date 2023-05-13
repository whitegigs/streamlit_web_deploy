import requests
import pandas as pd
# from bs4 import BeautifulSoup as bs
import streamlit as st



with open('css.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

i = 0
url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=부산관광&start={i}' 


# for i in range(1,30,10):
#     re = requests.get(url)
#     html = re.text
#     soup = bs(html,'html.parser')

#     news = soup.select('.news_tit')

#     for i in news:
#         title = i.text
#         link = i.attrs['href']
#         st.markdown(f'<ul><li><font size=2><a href="{link}">{title}</a>', unsafe_allow_html=True)




