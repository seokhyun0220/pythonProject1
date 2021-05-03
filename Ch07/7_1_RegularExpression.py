"""
날짜 : 2021/05/03
이름 : 강석현
내용 : 파이썬 졍규표현식 실습 교재 p192

정규표현식(Regular Expression)
 - 특정한 규칙을 갖는 문자열을 처리하기 위한 문법
 - 일반적으로 특정 문자 검색, 매치 여부를 확인할 때 정규표현식을 사용
"""

import re
from  re import findall, match


str1 = '1234 abc홍길동 ABC_555_6 부산광역시'

# 숫자검색
print(findall('1234', str1))
print(findall('[0-9]', str1))    # 0 ~ 9 번쨰 숫자
print(findall('[0-9]{3}', str1))  # 연속 3번만
print(findall('[0-9]{3,}', str1))   # 연속 3번 이상

# 문자열 검색
print(findall('[가-힣]{3,}', str1))  # 3자 이상 한글만
print(findall('[a-z|A-z]{3,}', str1))

str2 = 'test1abcABC 123mbc 45test'
print(findall('^test', str2))  # 맨앞에 test
print(findall('st$', str2))   # 마지막으로 끝나는 st

# 단어 검색
str3 = 'test^홍길동 abc 대한*민국 123$tbc'

print(findall('\\w{3,}', str3))  # 3자 이상 단어

# 응용
jumin = '123456-1891234'
result = match('[0-9]{6}-[1-2][0-9]{6}', jumin)  # 6번쨰자리가 1또는2가 와야된다

if result:
    print('주민번호가 맞습니다.')
else:
    print('주민번호가 아닙니다.')

