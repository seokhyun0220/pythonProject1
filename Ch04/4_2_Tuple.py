"""
날짜 : 2021/04/27
이름 : 김철학
내용 : 파이썬 자료구조 Tuple 실습 교재 p92
"""

#Tuple(고정 List) 생성  (추가,삭제 불가능)
tuple1 = (1,2,3,4,5)
print('tuple1 type :',type(tuple1))
print('tuple1[0] :', tuple1[0])
print('tuple1[4] :', tuple1[4])

tuple2 = ('서울','대전','대구','부산','광주')
print('tuple2 type :',type(tuple2))
print('tuple[0] : %s' % tuple2[0])
print('tuple[4] : {}' .format(tuple2[4]))

#tuple 수정 , 추가 ,삭제 x
tuple3 = 1, 2, 3, 4, 5
print('tuple3 type :', type(tuple3))

# tuple3[1] = 7 수정 x
# tuple3[4] = [] 삭제 x

