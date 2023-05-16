# 사용자가 반복의 시작과 끝을 입력하면 1씩 증가하는 반복문을 만들어 보자.
startNum = int(input('반복의 시작 입력:')) #1
endNum = int(input('반복의 끝 입력:')) #10

# 위에서 작성한 반복문을 이용해서 2씩 증가하는 반복문을 만들어 보자.
for i in range (startNum,(endNum+1)):
    print(i) #1,2,3,4,5,6,7,8,9,10

# 2씩 증가하겠다. 2씩 이상 증가하는 것은 생략 불가함. 단계가 1인 경우만 생략 가능
for i in range (startNum,(endNum+1),2):
    print(i)  #1,3,5,6,7,9

# 1에서 100까지의 정수 중 3의 배수에 해당하는 정수만 출력하는 코드를 작성하자.
for i in range(1,101):
    if i%3 ==0:
        print(i) #3,6,9,12.... .99


