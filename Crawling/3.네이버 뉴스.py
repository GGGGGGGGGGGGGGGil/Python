"""
날짜 : 2023/01/16
이름 : 길은섭
내용 : 파이썬 네이버 뉴스 크롤링 실습

 - 파이썬, 프로그램 등으로 접속하면 네이버에선 악성코드로 간주해서 접속 불가능
 - headers로 속여서 접속 가능
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import time

# HTML 요청
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text # headers로 유저 에이전트를(엔진) 정의해줘야 불러오기 가능
#print(html)

# 문서 객체 생성
dom = bs(html, 'html.parser')
tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
print('tit :', tit)

lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

for li in lis:
    title = li.select_one('dl > dt:not(.photo) > a').text
    print('title :', title.strip()) # strip 좌우 공백 없애줌