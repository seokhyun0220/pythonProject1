person = {'name':'홍길동', 'age': 35, 'address':'서울시'}
# (1) 요소 검사
print(person['age']) # 35
print('age' in person) # True

# (2) 요소 반복
for key in person.keys() :
    print(key) # key 출력
for v in person.values() :
    print(v)
for i in person.items():
    print(i)