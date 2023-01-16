"""
날짜 : 2023/01/16
이름 : 길은섭
내용 : 파이썬 HTML 요청 실습
"""
import requests as req

url = 'https://www.naver.com/'
html = req.get(url).text
print(html)
