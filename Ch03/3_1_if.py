"""
날짜 : 2021/04/27
이름 : 김철학
내용 : 파이썬 조건문 if 실습 교재 p68
"""
# if 파이썬에선 {} 안쓴다.
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 >0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')
        #위아래 같음 
if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')

# if ~ else (pass = 블록채움)
num3, num4 = 3, 4
if num3 > num4:
    # 조건이 참일때
    print('num3이 num4보다 크다.')
else:
    # 조건이 거짓일 때
    print('num3이 num4보다 작다.')

# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2는 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

# 삼항 조건문
num = 4

result =num * 2 if num >= 5 else num + 2

print('result :', result)

# 확인문제

score = int(input('점수 입력 :'))

print('점수 확인 :', score)

if score >= 90 and score <= 100:
    print('A 입니다.')
elif score >= 80 and score < 90:
    print('B 입니다.')
elif 70 <= score < 80:
    print('C 입니다.')
elif 60 <= score < 70:
    print('D 입니다.')
elif score < 60:
    print('F 입니다.')