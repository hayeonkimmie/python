# pi = 3.14
# radius = float(input('반지름(cm) 입력:'))
#
# circleArea = pi * radius * radius
# circleLength = 2 * pi * radius
#
# print('원의 넓이: %d' % circleArea)
# print('원의 둘레길이: %d' % circleLength)
#
# print('원의 넓이: %.1f' % circleArea)
# print('원의 둘레길이: %.1f' % circleLength)
#
#
# print('원의 넓이 \t: %d' % circleArea)
# print('원의 둘레길이 \t: %d' % circleLength)
#
# print('원의 넓이 \t: %.1f' % circleArea)
# print('원의 둘레길이 \t: %.1f' % circleLength)

name = input('이름 입력:')
mail = input('메일 입력:')
id = input('아이디 입력:')
password = input('비밀번호 입력:')
idNumber1 = input('주민번호 앞자리 입력:')
idNumber2 = input('주민번호 뒤자리 입력:')
address = input('주소 입력:')

print('-' *30)
print('이름 : {}'.format(name))
print('메일 : {}'.format(mail))
print('아이디 : {}'.format(id))
print('비밀번호 : {}'.format(len(password)))
print('주민번호 : {} - {}'.format(idNumber1, idNumber2))
print('주소 : {}'.format(address))


print(f'이름 : {name}')
print(f'메일 : {mail}')
print(f'아이디 : {id}')
pwStar = '*' * len(password)
print(f'패스워드: {pwStar}')
idNumber2Star = idNumber2[0] + ('*' * 6)

print(f'주민번호 : {idNumber1}-{idNumber2Star}')
print(f'주소 : {address}')



