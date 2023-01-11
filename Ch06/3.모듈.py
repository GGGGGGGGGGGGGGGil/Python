"""
날짜 : 2023/01/11
이름 : 길은섭
내용 : 파이썬 모듈 실습하기
 - 클래스는 클래스까지 선언하고 import해야하지만
 - 모듈은 바로 참조 가능
 - 파이썬은 객체를 모듈라고 함
 - 모듈 참조할때 변수 이름까지 써줘야함
 - 반드시 함수만 호출 가능한건 아님
"""
import sub2.calc
import sub2.calc as c
from sub2.calc import *

r1 = sub2.calc.plus(10, 20)
print('r1 :', r1)

r1 = c.plus(10, 20)
print('r1 :', r1)

r3 = multi(3, 4)
print('r3 :', r3)

r4 = div(4, 2)
print('r4 :', r4)


