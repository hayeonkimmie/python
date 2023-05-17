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
