import streamlit as st
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
import time
import random
import pandas as pd


st.set_page_config(layout="wide")

base="light"
secondaryBackgroundColor="#f1f1f1"
font="monospace"


st.title('오늘의 쿠팡')

# options = webdriver.ChromeOptions()
# options.add_argument('headless') # 헤드리스 모드 설정
# options.add_argument("--disable-gpu")
# time.sleep(5)

# now = datetime.now()
# today = now.strftime("%Y-%m-%d %H:%M:%S")
# st.text('오늘 날짜 '+ today)


keyword = st.text_input('검색할 물품을 입력하세요 :')
if st.button('조회'):
    # driver = webdriver.Chrome('chromedriver',chrome_options=options)
    time.sleep(5)
    driver = webdriver.Chrome('chromedriver')
    driver.get(f'https://www.coupang.com/np/search?component=&q={keyword}')
    time.sleep(5)
    html = driver.page_source  # 주소 적지 않아도 자동으로 긁어온다. page_source 
    source = bs(html,'html.parser')
    time.sleep(5)

    # 홍보성 광고물을 구분하고 싶다. 
    a = source.find_all('dl', class_='search-product-wrap')

    # 제품 이름
    name_list = []
    for i in a:
        name = i.find_all('div', class_='name')

        for j in name:
            name_list.append(j.text)

    # 가격
    price_list=[]
    for i in a:
        price = i.find_all('strong', class_='price-value')

        for j in price:
            price_list.append(j.text)

    # 도착예정
    arrival_list=[]
    for i in a:
        arrival = i.find_all('span', class_='arrival-info')

        for j in arrival:
            arrival_list.append(j.text.replace('  ',''))



            
    # 적립
    적립_list=[]
    for i in a:
        적립 = i.find_all('span', class_='reward-cash-txt')

        for j in 적립:
            적립_list.append(j.text.replace("최대 ",'').replace("원 적립",""))



    b = str(a).split('<dl class="search-product-wrap"><dt class="image"> <img alt="')[1:]
    ad = [''] * 36
    top_10=[''] * 36
    num = -1
    rank = 1
    for i in b:
        num += 1    # 첫번째 0 # 두번째 1
        if 'AD' in i:
            ad[num] = 'AD'
        # elif rank <= 10:    # 10위까지만 표시
            
        #     top_10[num] = rank
        #     rank += 1
        else:    # 한페이지에 있는 모든 물품에 대한 순위를 구한다. 
            top_10[num] = rank
            rank += 1

    # 평점
    star_list = []
    for i in range(36):
        try:
            star = b[i].split('%">')[1].split('<')[0]
            star_list.append(star)
        except:
            star_list.append('')
            
            
    # 리뷰
    review_list=[]
    for i in range(36):
        try:
            review = b[i].split('"rating-total-count">(')[1].split(')')[0]
            review_list.append(review)
        except:
            review_list.append('')


    #로켓배송
    로켓 = []
    for i in b:
        if '로켓배송' in i:
            로켓.append('로켓배송')
        elif '로켓직구' in i:
            로켓.append('로켓직구')
        else:
            로켓.append('')

    df = pd.DataFrame({"순위" : top_10,
        "광고" : ad,
        "제품" : name_list,
        "가격" : price_list,
        "최대 적립" : 적립_list,
        "평점" : star_list,
        "리뷰" : review_list,
        "로켓배송" : 로켓,
        "도착예정" : arrival_list})

    st.table(df)



