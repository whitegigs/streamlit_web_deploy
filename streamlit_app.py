import requests
import pandas as pd
import streamlit as st




st.title('오늘의 최신 부산 뉴스')



keyword = st.text_input('키워드를 입력하시면 [부산 + 키워드] 와 관련된 최신 뉴스 링크를 보여드립니다. 예) 아시아드 주 경기장, 북구 가볼만한 곳, 축제 등'," ")
st.write('부산관광 ', keyword)

# i = 0



for i in range(1,30,10):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=부산관광+{keyword}&start={i}' 
    re = requests.get(url)
    html = re.text
    soup = bs(html,'html.parser')

    news = soup.select('.news_tit')

    for i in news:
        title = i.text
        link = i.attrs['href']
        st.markdown(f'<ul><li><font size=2><a href="{link}">{title}</a>', unsafe_allow_html=True)
