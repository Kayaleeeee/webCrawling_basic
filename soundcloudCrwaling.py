import requests
from bs4 import BeautifulSoup

url = 'https://soundcloud.com/hm203es1hboe/sets/kayalee'
res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')

titles = soup.find_all(
    class_='trackItem__username sc-link-light')

print(titles)
