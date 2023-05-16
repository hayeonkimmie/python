# print('{} * {} = {}'.format(2,1,(2*1)))

for i in range (1,10)
    print('{} * {} = {}'.format(3,1,(3*1)))

for i in range (1,10):
    print('{} *{} = {}'.format(5,i,(5*i)))


print('{}선수 한테 메일 발송!!'.format('박찬호'))
print('{}선수 한테 메일 발송!!'.format('박세리'))
print('{}선수 한테 메일 발송!!'.format('박지성'))
print('{}선수 한테 메일 발송!!'.format('김연경'))
print('{}선수 한테 메일 발송!!'.format('이승엽'))

players =['박찬호, 박세리, 박지성, 김연경, 이승엽']
for player in players:
    print('{}선수 한테 메일 발송!!'.format(player))

#players에 각 개체들을 따옴표로 다 감싸주기. 그렇게 해야 리스트 내 한 객체를 하나씩으로 인정하여 구문을 반복해줌.
players = ['박찬호', '박세리','박지성', '김연경', '이승엽']
for player in players:
    print('{}선수 한테 메일 발송!!'.format(player))



