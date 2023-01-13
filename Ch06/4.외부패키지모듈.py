"""
날짜 : 2023/01/12
이름 : 길은섭
내용 : 파이썬 외부 패키지모듈 실습하기

패키지 설치
 - 터미널에 pip install openpyxl 쳐서 패키지 설치 
"""

from openpyxl import Workbook

# 새로운 엑셀파일 생성
workbook = Workbook()

# 현재 sheet 활성화
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '파이썬 Excel 실습'
sheet.append(['아이디', '이름', '휴대폰', '나이', '주소'])
sheet.append(['a101', '길은섭', '010-5357-8989', 27, '부산시'])
sheet.append(['a102', '이순신', '010-5357-8979', 37, '경주시'])
sheet.append(['a103', '장보고', '010-5357-8969', 47, '완도시'])

# 저장종료
workbook.save('C:/Users/java1/Desktop/member.xlsx')
workbook.close()

print('프로그램 종료...')