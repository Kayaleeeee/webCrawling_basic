import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/genre/bestChallenge.nhn'
res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')
title = soup.find_all(class_='challengeTitle')

print(title)
