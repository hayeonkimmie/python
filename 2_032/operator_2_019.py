char1='A' #65 ASCII CODE
char2='S' #83


# print('{}>{} : {}'.format(char1, char2, (char1>char2)))
# print('\'{}\'>'\{}\' : {}'.format(char1, char2, (char1>char2)))
#


print('\'A\' -> {}'.format(ord('A')))
print('\'a\' -> {}'.format(ord('a')))
print('\'s\' -> {}'.format(ord('s')))

print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))

chr(65)
chr(83)


str1='Hello'
str2='hello'
print('{}=={} : {}'.format(str1, str2,(str1==str2))) #False
print('{}=={} : {}'.format(str1, str2,(str1!=str2))) #True
#문자는 아스키코드로 변환해서 크기 비교 가능 하지만 문자열은 비교가 안되기 때문에 ㅐㅠol


userInputAlphabet=input('알파벳 입력:')
print('{}:{}'.format(userInputAlphabet, ord(userInputAlphabet)))

userInputASCII = int(input('아스키 코드 입력:'))
print('{}:{}'.format(userInputASCII, chr(userInputASCII)))
