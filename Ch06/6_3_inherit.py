"""
날짜 : 2021/04/29
이름 : 김철학
내용 : 파이썬 클래스 상속 실습하기 교재 p163
"""

from Ch06.sub2.StockAccount import StockAccount

kb = StockAccount('KB증권','106489-00-547865','김유신',10000,'삼성전자',10,10000)
kb.deposit(40000)
kb.withdraw(5000)
kb.buy(10, 80000)
kb.show()