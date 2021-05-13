"""
날짜 : 2021/05/13
이름 : 강석현
내용 : 코딩 테스트 - 숫자 카드 게임
"""

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
num = []
for i in range(n):
    arr = list(map(int, input().split()))
    num = min(arr)
    if num > result:
        result = num

print(result)