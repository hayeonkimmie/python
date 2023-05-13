
import operator

num1=8
num2=3
print('{} + {} = {}'.format(num1, num2, operator.sub(num1,num2)))
print('{} + {} = {}'.format(num1, num2, (num1+num2)))

print('{} + {} = {}'.format(num1, num2, operator.sub(num1,num2)))
print('{} - {} = {}'.format(num1, num2, operator.mul(num1,num2)))
print('{} * {} = {}'.format(num1, num2, operator.truediv(num1,num2)))
print('{} / {} = {}'.format(num1, num2, operator.mod(num1,num2)))
print('{} // {} = {}'.format(num1, num2, operator.floordiv(num1,num2)))
print('{} ** {} = {}'.format(num1, num2, operator.pow(num1,num2)))


print('{} == {} : {}'.format(num1, num2, operator.eq(num1, num2))) #equal
print('{} == {} : {}'.format(num1, num2, operator.ne(num1, num2))) #not equal
print('{} == {} : {}'.format(num1, num2, operator.gt(num1, num2))) #greater
print('{} == {} : {}'.format(num1, num2, operator.ge(num1, num2))) #greater equal



age = int(input('나이 입력'))
vaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65))

print('age: {}, vaccine : {}'.format(age, vaccine))



