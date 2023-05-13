import streamlit as st
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
import time
import random
from datetime import date
import pandas as pd



st.set_page_config(layout="wide")

base="light"
secondaryBackgroundColor="#f1f1f1"
font="monospace"


st.title('오늘의 쿠팡')
