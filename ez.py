#1부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합 그리고 팩토리얼을 출력하는 프로그램을 만들어 보자.

fNum = int(input('정수 입력:')) #사용자가 입력한 정수
addSum = 0 #정수까지의 합

for i in range(1, (fNum+1)): #사용자가 입력한 정수까지의 합 구하기
    addSum +=i

addSumFormated = format(addSum, ',') #형식 정리해주기
print('합 결과{}'.format(addSumFormated))

oddSum = 0

for i in range(1, (fNum+1)):
    if i %2 != 0:
        oddSum += i


oddSumFormated = format(oddSum, ',')
print('홀수 합 결과{}'.format(oddSumFormated))

evenSum = 0

for i in range(1, (fNum+1)):
    if i %2 == 0:
        evenSum += i


evenSumFormated = format(evenSum, ',')
print('짝수 합 결과{}'.format(evenSumFormated))

factorialResult = 1
for i in range(1, (fNum+1)):
    factorialResult*=i

factorialResult = format(factorialResult,',')
print('팩토리얼 결과: {}'.format(factorialResult))