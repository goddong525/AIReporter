import os.path
from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0'}

if not os.path.exists('../data'):
    os.mkdir('../data')

url = 'https://news.naver.com/'
request = Request(url, headers=headers)
response = urlopen(request, context=context)
html = response.read()

soup = BeautifulSoup(html, 'html.parser') #html 을 크롤링 할수 있는 형태로 가공
result = soup.find_all('div', {'class', 'cjs_t'}) #f12 누르면 나오는 class 로 n clicks nav . . .
titles = []

#for 문 . . . title 이 비어있는것들, 짧은 것들.... (10보다 작다면 무시하기)(필터링)
#통과된 것들만 titles 에 append 시켜서 titles.csv 에 저장했었음.

data = pd.DataFrame({'title': titles})
data.to_csv('../data/titles.csv', encoding='utf-8')

for r in result:
    print(r.text)
    titles.append(r.text)

print(titles)