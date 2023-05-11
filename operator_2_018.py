num1=10
num2=5
num1=10; num2=5

result = num1 > num2
print('num1>num2:{}'.format(result))

result= num1 >=num2
print('num1 > num2:{}'.format(result))

result=num1<num2
print('num1<num2:{}'.format(result))

result=num1<=num2
print('num1<=num2 :{}'.format(result))

result=num1 !=num2
print('num1!=num2 : {}'.format(result))

userInputNumber1=int(input('첫번 째 숫자 입력:'))
userInputNumber2 =int(input('두번 째 숫자 입력:'))
print('{}>{}: {}'.format(userInputNumber1, userInputNumber2, (userInputNumber1>userInputNumber2)))


maxLength=5200
maxWidth=1985
myCarLength=int( input('천장 길이 입력:'))
myCarWidth=int( input('전폭 길이 입력:'))
print('천장 가능 여부 :{}'.format(myCarLength<= maxLength))
print('전폭 가능 여부 :{}'.format(myCarWidth<= maxWidth))
