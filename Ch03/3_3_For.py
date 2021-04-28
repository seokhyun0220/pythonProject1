"""
날짜 : 2021/04/27
이름 : 김철학
내용 : 파이썬 반복문 For 실습 교재 p70
"""

# For
for i in range(5):
    print('i :', i)

for j in range(10,20): # 10부터 19까지
    print('j :', j)

for k in range(10, 0, -1):
    print('k :', k)   # 10부터 0까지 -1 차감

# 1부터 10까지 합
sum1 = 0

for k in range(11):
    sum1 += k

print('1부터 10까지 합 :', sum1)

# 1부터 10까지 짝수합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k

print('1부터 10까지 짝수합 :', sum2)

# 중첩 For
for a in range(3):
    print('a :', a)
    for b in range(4):
        print('b :', b)

# 구구단
for x in range(2, 10):
    
    print(x, '단')
    
    for y in range(1, 10):
        z = x * y
        print('%d x %d = %d' % (x, y, z) )

# 별삼각형
for a in range(10,0,-1):

    for b in range(a):

        print('☆', end='')

    print() # 줄 바꿈

for i in range(10):
    print('★' * i)

# List를 이용한 For - I
nums = [1,2,3,4,5]

for num in nums:
    print('num :', num)

for person in ['김유신', '김춘추', '장보고']:
    print('person :', person)

scores = [62,86,72,74,96]
total = 0

for score in scores:
    total += score

print('score의 총합 :', total)

# List index, value 출력
for index, value in enumerate(scores):
    print('{},{}'.format (index, value) )

# List comprehension
List1 = [1,2,3,4,5]

List2 = [num * 2 for num in List1]
List3 = [num * 3 for num in List1 if num % 2 == 1]

print('List2 :', List2)
print('List3 :', List3)