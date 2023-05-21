for i in range (1,10):
    for j in range(i):
        print('*', end='')
#     print()
#
#
for i in range(10,0, -1):
    for j in range(i):
        print('*', end='')
    print()


#반복 안에 또 다른 반복이 있는 것이기 때문에 구상을 잘 해야 함.
for i in range(1,10):
    for j in range(2,10):
        result = j* i
        print('{} * {} = {} \t'.format(j, i ,result), end='')

    print()