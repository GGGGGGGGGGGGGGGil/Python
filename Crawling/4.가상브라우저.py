"""
날짜 : 2023/01/17
이름 : 길은섭
내용 : 파이썬 크롤링 고급기법 가상브라우저 실습

 - selenium 패키지 다운
 - chromedriver 가서 크롬 버전에 맞는 버전으로 다운 (ChromeDriver 109.0.5414.74) 
 - chromedriver.exe 실행기 파이썬 폴더에 드래그해서 추가
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

## 가상브라우저 실행

# 가상브라우저 강제종료 해결
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 가상브라우저로 네이버 이동
browser.get('https://naver.com')

# 로그인 클릭
btnLogin = browser.find_element(By.CSS_SELECTOR, '#account > a')
btnLogin.click()

# 아이디/비번 입력
input_id = browser.find_element(By.CSS_SELECTOR, '#id')
input_pw = browser.find_element(By.CSS_SELECTOR, '#pw')

input_id.send_keys('abcd')
input_pw.send_keys('1234')

# 최종 로그인 클릭
btnSubmit = browser.find_element(By.CSS_SELECTOR, '#log\.login')
btnSubmit.click()
