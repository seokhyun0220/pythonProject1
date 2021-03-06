# (1) 중첩함수 정의
def main_func(num):
    num_va1 = num  # 자료 생성
    def getter():  # 획득자 함수, return 있음
        return num_va1
    def setter(value): # 지정자 함수 인수 있음
        nonlocal num_va1 # nonlocal 명령어
        num_va1 = value

    return getter, setter  # 함수 클로저 반환

# (2) 외부 함수 호춯
getter, setter = main_func(100)  # num생성

# (3) 획득자 호출
print('num =', getter())  # 획득한 num 확인

# (4) 지정자 획득
setter(200)  # num 값 수정
print('num =', getter())  # num 수정 확인