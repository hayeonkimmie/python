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

