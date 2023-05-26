import datetime
today = datetime.datetime.today() #날짜, 실시간 시간 다 나옴. 2023-03-06 21:46:42.527218

day = today.day #날짜만 뽑아낼 수 있음.
limitDust = 150
dustNum = int(input('미세먼지 수치 입력: ')) #실행문 숫자 비교를 위해, int로 형변환 해주기
carType = int(input('차량 종류 선택: 1. 승용차 2. 영업용차'))
carNumber = int(input('차량 번호 입력:'))

print('-' * 30)
print(today)
print('-' * 30)
# 나중에 실행문 코딩하고 싶을 때는 pass입력해두고 일단 넘어가기
# if dustNum >= limitDust and carType ==1:
#     pass
# if dustNum >= limitDust and carType ==2:
#     pass

if dustNum >limitDust and carType ==1:
    if (day %2) == (carNumber %2):
        print('차량 2부제 적용')
        print('차량 2부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dustNum > limitDust and carType ==2:
    if (day %5) == (carNumber %5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dustNum <=limitDust :
    if (day %5) == (carNumber %5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')
