"""
날짜 : 2023/01/18
이름 : 길은섭
내용 : 파이썬 기상청 가상브라우저 실습

 - selenium 패키지 다운
 - chromedriver 가서 크롬 버전에 맞는 버전으로 다운 (ChromeDriver 109.0.5414.74) 
 - chromedriver.exe 실행기 파이썬 폴더에 드래그해서 추가
"""
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

## 가상 브라우저 실행

# 가상 브라우저 강제종료 해결
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 기상청 이동
browser.get('https://www.kma.go.kr/w/obs-climate/land/city-obs.do')

# 전국 도시명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    print(tds[0].text)
    

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234',
                        db='java1db', 
                        charset='utf8')
cur = conn.cursor()

# SQL 실행
for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR,'td')
    var = []

    for i in tds:
        if i.text == ' ':
            var.append(None)
        else:
            var.append(i.text)
        sql = "insert into `weather` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    cur.execute(sql, var)
    conn.commit()   

# 데이터베이스 & 가상 브라우저 종료
conn.close()
browser.close()

print('데이더베이스 등록 완료...')
print('프로그램 종료...')
