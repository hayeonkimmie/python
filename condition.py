# exampleScore = int(input('시험 성적 입력:'))
# grades =''
#
# if exampleScore >= 90:
#     grades ='A'
# elif exampleScore >=80:
#     grades='B'
# elif exampleScore >=70 :
#     grades='C'
# elif exampleScore >=60:
#     grades='D'
# else:
#     grades='F'
#
# print('성적 :{}\t 학점:{}'.format(exampleScore, grades))


print('1. 카페라떼 (3.5) \t 2. 에스프레소(3.0) \t 3. 아메리카노 (2.0) \t 4. 곡물라떼 (4.0) \t 5. 밀크티(4.3)')
userSelectNumber = int(input('메뉴 선택:'))

print ('-' * 43)
if userSelectNumber ==1:
    print('메뉴 : 카페라떼')
    print('가격 : 3,500원')

elif userSelectNumber == 2:
    print('메뉴 : 에스프레소')
    print('가격 : 3,000원')

elif userSelectNumber == 3:
    print('메뉴 : 아메리카노')
    print('가격 : 2,000원')

elif userSelectNumber == 4:
    print('메뉴 : 곡물라떼')
    print('가격 : 4,000원')

elif userSelectNumber == 5:
    print('메뉴 : 밀크티')
    print('가격 : 4,300원')
print('-' * 43)