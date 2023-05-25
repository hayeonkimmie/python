#random module 은 난수를 발생시켜주는 뛰어난 모듈
import random

# import random
# comNum = random.randint(1,2) #1,2 선택 가능 둘중에 하나. 컴퓨터가 가지고 있는 숫자.
# userSelect = int(input('홀/짝 선택: 1. 홀 \t 2. 짝')) # int로 형변환 해주어야 비교연산 가능.데이터는 문자인데 숫자로 비교 불가능.
#
# if comNum ==1 and userSelect == 1:
#     print('빙고!! 홀수!!')
# elif comNum ==2 and userSelect ==2:
#     print('빙고!! 짝수!!')
# elif comNum ==1 and userSelect ==2:
#     print('실패!! 홀수!!')
# elif comNum ==2 and userSelect ==1:
#     print('실패!! 짝수!!')


#가위바위보 게임
comNumber = random.randint(1,3)
userNumber = int(input('가위, 바위, 보 선택 : 1. 가위 \t 2. 바위 \t 3. 보'))

if (comNumber ==1 and userNumber ==2) or (comNumber ==2 and userNumber ==3) or (comNumber==3 and userNumber ==1):
    print('컴퓨터 : 패, 유저 : 승')
elif comNumber == userNumber :
    print('무승부')
else:
    print('컴퓨터: 승, 유저 : 패')

print('컴퓨터: {}, 유저:{}'.format(comNumber, userNumber))
