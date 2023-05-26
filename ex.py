
str = '*'
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()



for i1 in range (1,6):
    for i2 in range (6-i1 -1):
        print(' ',end ='')
    for i3 in range(i1):
        print('*', end='')

    print()


for i in range(5,0,-1): #단계가 줄어드는 것
    for j in range(i):
        print('*', end='')
    print()

 # for i in range (5,0,-1):
 #    for j in range(5-i):
 #        print(' ', end ='') #공백 찍고 끝에는 개행하지 마라.
 #
 #    for j in range(i):
 #        print('*', end='')




for i in range(1,10):
    if i<5 :
        for j in range(i): #증가하니까 i만큼 출력
            print('*', end='')

    else:
        for j in range(10-i):
            print('*', end='')

    print()


    print()



for i in range(1,6): #i는 행을 나타내는 숫자.
    for j in range(1, 6):
        if j == i:
            print('*', end='')
    else:
        print('*', end='')

    print()