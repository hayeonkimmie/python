# rainPercentage = int(input('비율 확률 입력:'))
# minRainPercentage = 55
#
# print('우산 챙기세요.') if rainPercentage >= minRainPercentage else print('양산 챙기세요')
#
# if rainPercentage >=minRainPercentage:
#     print('우산 챙기세요')
# else:
#     print('양산 챙기세요')



lowTemp = int(input('최저 기온 입력:'))
highTemp = int(input('최고 기온 입력:'))

tempDifference = highTemp - lowTemp
if tempDifference>=11:
    print('감기 조심하세요')
else:
    print('산책하기 좋은 날씨 입니다.')