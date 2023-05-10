# # num1=10
# # num2=20
# # result=num1+num2
# #
# # print(result)
# #
# # print('num: {}'.format(n+=3))
# num1=10
# num1 += 3 #num1 = num1+3
# print('num :{}'.format(num1))
#
#
# num1=10
# num1 /= 3 #num1 = num1+3
# print('num :{}'.format(num1))
# #나누면 항상 float type
#
# num=10
# num//=3
# print('num:{}'.format(num))
#
# num=10
# num**=3
# print('num:{}'.format(num))


rainAmount = 0
totalRainAmount=0

totalRainAmount += 30
print('1월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 45
print('2월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 122
print('3월 누적 강수량: {}mm'.format(totalRainAmount))

totalRainAmount += 177
print('4월 누적 강수량: {}mm'.format(totalRainAmount))

print('-' *30)
print('연간 누적 강수량:{}'.format(totalRainAmount))
print('-'*30)

print('연간 평균 강수량: {}mm'.format(totalRainAmount/rainAvgAmount))