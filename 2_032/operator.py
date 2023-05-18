# if 10 > 5 : #이 조건문이 트루인 경우에, 실행함.
#     print ('10은 5보다 크다.')
#     print('또 다른 실행문 !!')
#
# print('조건문이 끝났어요,')
#
#
# num1= 10
# num2 = 20
#
# if num1 == num2:
#     print('num1<=num2') #거짓이니까 실행이 안 됨.

korScore = int(input('국어 점수:'))
matScore = int(input('수학 점수:'))
engScore = int(input('영어 점수:'))


avgScore = (korScore + matScore + engScore) /3
print('평균 : {}'.format(avgScore))
if avgScore >= 90:
    print('참 잘했어요~')


highTemperature = 28
lowTemperature = 20

innerTemperature = int(input('실내 온도 입력:'))
if innerTemperature >= highTemperature:
    print('냉방 작동!')

if innerTemperature <= lowTemperature:
    print('난방 작동!')