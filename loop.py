
#조건식에 논리형 데이터를 사용해서 무한 반복 실행할 수 있다. 무한루프
flag=True
num=0
sum=0
while flag :
    num +=1
    sum += num
    print('{}까지의 합은 {}입니다.'.format(num, sum))

    if sum >=1000:
        flag = False # flag변수를 false로 바꿔라
#논리형 타입을 사용하여 사용을 제한할 수 있음. sum이 1000이상 되면 반복문 멈춤.

#하루에 독감으로 병원에 내방하는 환자 수가 50명에서 100명 사이일 때, 누적 독감 환자 수가 최초 10,000명을 넘는 날짜를 구해보자.
import random
sum =0
date = 0
flag =True

while flag:
    patientCount = random.randint(50,100) #내방하는 환자 수 50-100명 사이.
    sum += patientCount
    date+=1
    print('날짜 : {} \t 오늘 환자 수: {} \t 누적 환자 수: {}'.format(date, patientCount, sum))

    if sum >=10000:   #누적 독감 환자 수 최초 10000명일 때 반복문 멈추기.
        flag= False
