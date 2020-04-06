# API & WEB CRAWLING

## 웹 크롤링

- **크롤링이 불법인지 확인하기 :**
  ulr + /robots.txt에서 확인
  disallow하는 부분은 상업적으로 크롤링 금지

- **Beautiful Soup 이용**

  - Python 패키지로 HTML에서 데이터를 추출하는데 사용
  - install하기: pip3 install bs4
  - Library

    - find(): 가장 먼저 검색된 것 크롤링
    - find_all(): 전체
    - html.parser: html에서 데이터 추출해오기

    ```python
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

        //class에서 title만 추출해오기//

    print(title_array)
    ```
