# (1) 일급 함수
def a ():  # outer
    print('a 함수')
    def b ():  # inter
        print('b 함수')
    return b
b = a()   # 외부 함수 호출 : a 함수
b()   # 내부 함수 호출 : b 함수

# (2) 함수 클로저
data = list(range(1, 101))
def outer_func(data):
    dataset = data   # 값(1~100) 생성
    # inter
    def tot ():
        tot_va1 = sum(dataset)
        return tot_va1
    def avg(tot_va1):
        avg_va1 = tot_va1 / len(dataset)
        return  avg_va1
    return tot, avg  # inter 변환

# 외부 함수 호출 : data 생성
tot, avg = outer_func(data)

# 내부 함수 호출
tot_va1 = tot ()
print('tot =', tot_va1)
avg_va1 = avg(tot_va1)
print('avg =', avg_va1)