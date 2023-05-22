# userMsg=input('메시지 입력:')
# print('메시지 문자열 길이 :{}'.format(len(userMsg)))


article = '파이썬(영어:Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로,객체지향'

strIdx = article.find('객체지향')
print('\'객체지향\' 문자열 위치 : {}'.format(strIdx))

width= float(input('가로 길이 입력:'))
height = float(input('세로 길이 입력:'))

triangleArea = width * height /2
squareArea = width * height

print('-' * 25)
print('삼각형 넓이 : %f' %triangleArea)
print('사각형 넓이 : %f' %squareArea)

print('삼각형 넓이 : %.2f' %triangleArea)
print('사각형 넓이 : %.2f' %squareArea)
print ('-' * 25)
print('삼각형 넓이 : %.3f' %triangleArea)
print('사각형 넓이 : %.3f' %squareArea)