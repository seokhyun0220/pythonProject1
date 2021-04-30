fat = int(input("지방의 그램을 입력하세요"))

car = int(input("탄수화물의 그램을 입력하세요"))

protein = int(input("단백질의 그램을 입력하세요"))

totcar = fat * 9 + protein * 4 + car * 4

print('총칼로리 :', totcar)

frist = input("첫번째 단어")
second = input("두번째 단어")
third = input("세번째 단어")


Abbreviation = frist[0] + second[0] + third[0]

print('====================')
print('약자 :', Abbreviation.upper())