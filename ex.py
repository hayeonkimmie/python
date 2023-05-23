# hour = int(input('시간 입력:'))
# min = int(input('분 입력:'))
# sec = int(input('초 입력:'))
# print('{}초'.format(hour*60*60+min*60+sec))
#
# # , 이용하여 가독성을 높이기 위해 format함수 재사용. , 를 사용하면 숫자가 문자 형태로 변환됨.
# print('{}초'.format(format(hour*60*60+min*60+sec, ',')))
#

money = int(input('금액 입력:'))
rate = float(input('이율 입력:'))
term = int(input('기간 입력:'))

targetMoney = money

for i in range(term):
    #targetMoney=targetMoney + (targetMoney * rate * 0.01)

    targetMoney+= (targetMoney * rate * 0.01)

    #1000단위로 끊어줌
targetMoneyFormated = format(int(targetMoney), ',')
print('-' *30)
print('이율:{}'.format(rate))
print('원금:{}'.format(format(money,',')))
print('{}년 후 금액:{}'.format(term, targetMoneyFormated))
