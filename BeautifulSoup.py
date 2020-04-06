import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query='
query = input('Please enter the keyword to search : ')
FullURL = URL + query

data = requests.get(FullURL).text
soup = BeautifulSoup(data, 'html.parser')
news_title = soup.find_all(class_='_sp_each_title')
title_array = []

for title in news_title:
    title_array.append(title.get('title'))
print(title_array)
