"""
날짜 : 2023/01/11
이름 : 길은섭
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car
from sub1.Account import Account

# 객체지향
BMW = Car('BMW', '검정색', 50000)
BMW.speedUp()
BMW.speedDown()
BMW.show()

sonata = Car('sonata', '흰색', 10000000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

kb = Account('국민은행', '351-21-1001', '길은섭', 10000)
kb.deposit(50000)
kb.withdraw(5000)
kb.balance += 5000
kb.show()

wr = Account('우리은행', '444-44-5555', '장보고', 1000000000)
wr.deposit(1000)
wr.withdraw(850456238)
wr.show()

# 캡슐화
#kb.__balance += 5000
kb.show()

wr = Account('우리은행', '444-44-5555', '장보고', 1000000000)
wr.deposit(1000)
wr.withdraw(850456238)
wr.show()

