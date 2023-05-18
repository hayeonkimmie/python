#횟수에 의한 반복. 1부터 10까지의 합을 구하는 경우
sum=0
for i in range(1,11):
    sum +=1 #sum에 1을 누적하면서 for문을 루프 돌면서 반복.
print('sum : {}'.format(sum))

#while문을 사용한 반복문. 1부터 10까지의 합
sum=0
n=1 #n이 무엇인지 모름.
while n<11:
    sum +=n
    n+=1

print('sum: {}'.format(sum))

#for문이 while문보다 코드가 더 간결. 횟수에 의한 반복이기 때문

#1부터 시작해서 7의 배수의 합이 50 이상인 최초의 정수 출력
sum = 0
maxInt = 0 #최초의 정수

for i in range(1,101):
    if i%7 ==0 and sum <=50:
        sum += 1
        maxInt =1

        print('i: {}'.format(i))
print(' 7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(maxInt))


sum = 0
maxInt =0
n =1
while n<=100 and sum <=50:
    n+=1

    if n%7 ==0: #7의 배수이면
        sum += n #반복문 실행시키기
        maxInt = n #최초의 정수값 구하기

    print('n: {}'.format(n))


print('7의 배수의 합이 50 이상인 최초의 정수: {}'.format(maxInt))


# 다음 반복 실행을 위해서 for문과 while문 중 가장 적합한 구문을 이용해서 프로그램을 만들어 보자.
# 자동차 바퀴가 한번 구를 때마다 0.15mm씩 마모된다고 한다.
# 현재의 바퀴 두께가 30mm이고 최소 운행 가능 바쿼 두께가 20mm라고 할 때 앞으로 구를 수 있는 횟수를 구해보자.
currentThickness=30
rotationCount=0
removeThickness=0.15

while currentThickness >= 20:
    rotationCount +=1
    currentThickness -= removeThickness

safeRotationCount = rotationCount -1
print('운행 가능 횟수 : {}'.format(safeRotationCount))
