"""
날짜 : 2021/05/13
이름 : 강석현
내용 : 코딩 테스트 - 큰 수의 법칙
"""

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구반하여 입력받기
date = list(map(int, input().split()))

# 리스트를 내림차순으로 정렬
date.sort(reverse=True)

# 제일 큰 수
first = date[0]

# 두번째로 큰수
second = date[1]

result = 0

while True:
    for i in range(k):
        result += first
        m -= 1
        if m == 0:
            break
            result += second
            m -= 1
            if m == 0:
                break

    print(result)


