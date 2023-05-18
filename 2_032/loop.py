<<<<<<< HEAD
num=0

while True :
    print('Hello')
    num +=1
    if num >=5:
        break  #반복문 종료
print('THE END!!')

sum = 0
searchNum =0
for i in range(100):
    sum += i

    if sum >100:
        searchNum = i #100 이 넘었을 때 i가 무엇인지 알고 싶은 것
        break

print('searchNum : {}'.format(searchNum))

# 10의 팩토리얼(10!)을 계산하는 과정에서 결과값이 50을 넘을 때의 숫자를 구하자.
result = 1
num=0
for i in range(1,11):
    result *= i

    if result >50:
        num = i
        break

print('num : {}, result :{}'.format( num, result)) #num : 5, result : 120

# 새끼 강아지 체중이 2.2kg가 넘으면 이유식을 중단하려고 한다. 한번 이유식을 먹을 때 체중이 70g 증가한다고 할 때,
# 예상되는 이유식 날짜를 구하자. (현재 체중은 800g이다.)
limitWeight= 2200
currentWeight=800
date=1

while True:
    if currentWeight >=2200:
        break


    date +=1
    currentWeight +=70
print("이유식 중단 날짜 : {}일".format(date)) #21

=======
endNum = 10
n=0

# infinite loop
# while n <= endNum :  - 0은 10보다 항상 작기 때문에 무한루프에 빠짐.
#     print(n)
while n<= endNum:
    print(n)
    n +=1

#n이 10이하이면 반복 실행 - 구구단 중 7단
n=1
while n<=10:
    result = 7 * n
    print('{} * {} = {}'.format(7,n, result))
    n+=1


n=0
while n<10:
    pass #언젠가는 코딩 할텐데 당장은 하지 않겠다. 오류를 내지말고 일단 패스.

while n<10:
    print('hello')
    print('hi')
    n+=1

#1부터 100까지 정수 중 2의 배수와 3의 배수를 구분해서 출력하자.
n=1
while n<101:
    if n%2 == 0:
        print('{}은 2의 배수이다.'.format(n))

    if n%3 ==0:
        print('{}은 3의 배수이다.'.format(n))
    n+=1

n=1
while n<101:
    if n%2 ==0:
        print('{}은 2의 배수이다'.format(n))
    if n%3 ==0:
        print('{}은 3의 배수이다.'.format(n))
    n+=1
>>>>>>> 42730f0 (loop_2_032)
