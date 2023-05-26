#프로그램을 반복 실행하기 위한 반복문
#1부터 100까지 정수 중 십의자리와 일의자리에 대해 각각 홀/짝수를 구분하는 프로그램을 만들어 보자.
# for i in range(1,101):
#     print(i) #1~100 까지 출력 됨

for i in range(1, 101):
    if i <=9:
        if i %2 == 0:
            print('[{}] : 짝수!'.format(i))
        else:
            print('[{}] : 홀수!'.format(i))

    else:
        num10 = i//10
        num1=i%10

        result10 = ''
        if num10 %2 ==0:
            result10 ='짝수'
        else:
            result10='홀수'

        result1 = '0'
        if num1 != 0:
            if num1 %2 ==0:
                result1 ='짝수'
            else:
                result1='홀수'


        print('[{}] 십의자리 : {}, 일의자리 :{}'.format(i, result10, result1))
# 프로그램을 반복 실행하기 위한 반복문
# 1부터 100까지 정수 중 십의자리와 일의자리에 대해 각각 홀/짝수를 구분하는 프로그램을 만들어 보자.
# for i in range(1,101):
#     print(i) #1~100 까지 출력 됨
for i in range(1,101):
    if i<=9:
        if i %2 ==0:
            print('[{}] :  짝수!!'.format(i))
        else:
            print('[{}] : 홀수!!'.format(i))

    else:
        num10 = i//10
        num1 =i%10

        result10=''
        if num10 %2 ==0:
            result10 = '짝수'
        else:
            result10 = '홀수'
        result1 = '0'
        if result1 != 0:
            if num1 % 2==0:
                result1='짝수'
            else:
                result1= '홀수'