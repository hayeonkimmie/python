# speed= int(input('속도 입력:'))
# if speed > 50:
#     print('안전속도 위반!! 과태표 50,000원 부과 대상!!!')
# else:
#     print('안전속도 준수!!')


# inputMsg = input('메시지 입력:')
# lengthMsg = len(inputMsg)
# if len(inputMsg) <=50:
#     print('SMS 발송!!')
#     print('메시지 길이 : {}'.format(lengthMsg))
#     print('메시지 발송 요금: 50원')
# else:
#     print('MMS 발송!!')
#     print('메시지 길이 : {}'.format(lengthMsg))
#     print('메시지 발송 요금: 100원')


message = input('메시지 입력:')
lenMessage = len(message)
msgPrice = 50

if lenMessage <= 50:
    msgPrice = 50
    print('SMS 발송!!')

if lenMessage >50:
    msgPrice = 100
    print('MMS 발송!!')

print('메시지 길이 : {}'.format(lenMessage))
print('메시지 발송 요금: {}'.format(msgPrice))

ㄷ