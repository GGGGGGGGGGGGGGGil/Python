""" Crawling 연습 """
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

# 백준 HTML 요청 연습
url = 'https://www.acmicpc.net/step/1'
html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
# print(html)

# 문서객체 생성
dom = bs(html, 'html.parser')

#문서 파싱 연습
div = dom.html.head.title
con = dom.select_one('.pull-left').text
tds = dom.select('td > a')

print('div :', div)
print('con :', con)

for td in tds:
    print('td text :', td.text)


# 네이버 뉴스 HTML 요청 연습
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text

# 문서 객체 생성
dom = bs(html, 'html.parser')
tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
print('tit :', tit)

sps = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

for sp in sps:
    span = sp.select_one('dd > span:not(.date)').text
    print('span :', span.strip())