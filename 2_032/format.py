userName='Hong gil dong'
userAge=21
print('User name: {}'.format(userName))
print('User age: {}'.format(userAge))
print('User name: {}, User age : {}'.format(userName, userAge)) #한 줄에 출력됨

print('User name: {1}, User age : {0}'.format(userName, userAge)) #인덱스 넘버를 강제적으로 넣어서 순서를 바꿔줄 수 있음

print('나의 이름은 {}이고, 나이는 {}살 입니다. {}이름은 아버님께서 지어 주셨습니다'.format(userName, userAge, userName))
print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0}이름은 아버님께서 지어 주셨습니다'.format(userName, userAge))

print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0}이름은 아버님께서 지어 주셨습니다'
      .format(userName, userAge))


print('User name: %s' %userName)#문자니까 s
print('User age: %d' %userAge)
print('User name : %s, User age: %d' %(userName, userAge))

pi=3.14
print('pi: %f' %pi)
print('pi: %.1f' %pi) #소숫점 첫재짜리까지 출력
print('pi: %d' %pi) #정수로 출력

radius=float(input('반지름 입력:'))
pi=float(input('원주율 입력'))
print('radius: %.2f' %radius)
print('pi %f' %pi)
print('pi %.2f' %pi)



circleArea = radius * radius * pi
print('radius : %.2f' %radius)
print('pi: %.2f' %pi)

print('circleArea: %.2f' %circleArea)

num1= 3.14
num2= 0.12
print('num1+num2=%.2f')




