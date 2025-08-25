# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:52:18 2023

@author: Admin
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://udn.com/news/cate/2/7227")

soup = BeautifulSoup(browser.page_source,'html.parser')
item = soup.find('section',class_=\
                 'thumb-news more-news thumb-news--big context-box')
# print(item)   
item2 = item.find_all('div',class_='story-list__news')
# print(item2)
count = 0
for i in item2:
    count = count+1
    title = i.find('h3').text
    title = title.replace('\n','')
    newstime = i.find('time',class_='story-list__time').text
    print('編號: ',count)
    print(title,' ', newstime)
    print()


for i in range(6):
    time.sleep(3)
    # '空白'要用 '點' 代替
    inputElement = browser.find_element(By.CLASS_NAME,\
    "btn.btn-ripple.btn-more.btn-more--news")
    # 定位.click() 控制滑鼠點下去
    inputElement.click()
    
    
soup = BeautifulSoup(browser.page_source,'html.parser')
item = soup.find('section',class_=\
                  'story-list__holder--append')
# print(item)   
item2 = item.find_all('div',class_='story-list__news')
# print(item2)
for i in item2:
    count = count+1
    print('編號: ',count)
    title = i.find('story-list__text').find('a').text
    title = title.replace('\n','')
    newstime = i.find('time',class_='story-list__time').text.replace('\n','')
    print(title+' '+newstime)
    print()

