# num1=2
# num2=3
# result=num1 ** num2
# print('result: {}'.format(result))
#
# num1= 7
# num2= 5
# result=num1 *num2

# #2의 2 제곱근
# result=2**(1/2)
# print('result: %.2f' %result)
# # #2의 3제곱근
# result=2**(1/3)
# print('result: %.2f' %result)
# #
# #  #2의 4제곱근
# result=2**(1/4)
# print('result: %.2f' %result)

import math
print(math.sqrt(5))
print(math.pow(4,8))

firstMonthMoney=200
after12Month = ((firstMonthMoney*0.01)**12)*100
print('12갸월 후 용돈: {}'.format(after12Month))

after12Month=int(after12Month)
strResult=format(after12Month, ',')
print(strResult, '원')