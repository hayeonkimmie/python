part = int(input('업종 선택 (1. 가정용 \t 2. 대중탕용 \t 3. 공업용) :'))
useWater = int(input('사용량 입력:'))
unitPrice = 0 #업종에 따라서 단가 달라지기 때문에 일단 0으로 설정

if part ==1:
    unitPrice = 540
elif part ==2:
    if useWater <= 50:
        unitPrice = 820
    elif useWater > 50 and useWater <= 300:
        unitPrice = 1920
    elif useWater > 300 :
        unitPrice = 2400
    pass

elif part == 3:
    if useWater <=500:
        unitPrice = 240
    else:
        unitPrice = 470

print('*' *30)
print('상수도 요금표')
print('-' * 30)
print('사용량 \t : \t 요금')

userPrice = useWater * unitPrice
print('{} \t : \t {}원'.format(useWater, userPrice))
print('=' *50)
