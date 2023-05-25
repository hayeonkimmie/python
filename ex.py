# koreanScore=int(input('국어 점수:'))
# engScore=int(input('영어 점수:'))
# matScore=int(input('수학 점수:'))
# sciScore=int(input('과학 점수:'))
# hisScore=int(input('국사 점수:'))
#
# totalScore = koreanScore + engScore + matScore + sciScore + hisScore
# avgScore = totalScore/5
# difference =
#
# print('-'*50)
#
# print('총점 : {}({}), 평균 :{}({})'format(totalScore, avgScore))
#
# engScore
# matScore
# matScore
# sciScore
#
korAvg = 85; engAvg = 82; matAvg = 89
sciAvg = 75; hiAvg = 94

totalAvg = korAvg + engAvg + matAvg + sciAvg + hiAvg
avgAvg = int(totalAvg/ 5)

korScore = int(input('국어 점수:'))
engScore = int(input('영어 점수:'))
matScore = int(input('수학 점수:'))
sciScore = int(input('과학 점수:'))
hiScore = int(input('국사 점수:'))


totalScore = korScore + engScore + matScore + sciScore + hiScore
avgScore = int(totalScore/5)

korGap = korScore - korAvg
engGap = engScore - engAvg
matGap = matScore - matAvg
sciGap = sciScore - sciAvg
hiGap = hiScore - hiAvg

totalGap = totalScore - totalAvg
avgGap = avgScore - avgAvg

print('-' * 70)
print('총점 : {}({}), 평균 : {}({})'.format(totalScore, totalGap, avgScore, avgGap))
print('국어 : {}({}), 영어 : {}({}), 수학 : {}({}), 과학 : {}({}), 국사: {}({})'.format(
    korScore, korGap, engScore, engGap, matScore, matGap, sciScore, sciGap, hiScore, hiGap))

print('-' * 70)

str = '*' if korGap > 0 else '-'
print('국어 편차 : {}({})'.format(str * abs(korGap), korGap))  # abs : 절대값 구하는 함수. - 수를 곱하면 0이기 때문
str = '*' if engGap > 0 else '-'
print('영어 편차 : {}({})'.format(str * abs(engGap), engGap))  # abs : 절대값 구하는 함수. - 수를 곱하면 0이기 때문
str = '*' if matGap > 0 else '-'
print('수학 편차 : {}({})'.format(str * abs(matGap), matGap))  # abs : 절대값 구하는 함수. - 수를 곱하면 0이기 때문
str = '*' if sciGap > 0 else '-'
print('과학 편차 : {}({})'.format(str * abs(sciGap), sciGap))  # abs : 절대값 구하는 함수. - 수를 곱하면 0이기 때문
str = '*' if hiGap > 0 else '-'
print('국사 편차 : {}({})'.format(str * abs(hiGap), hiGap))  # abs : 절대값 구하는 함수. - 수를 곱하면 0이기 때문

str = '*' if totalGap >0 else '-'
print('총점 편차 : {}({})'.format(str * abs(totalGap), totalGap))

str = '*' if avgGap >0 else '-'
print('평균 편차 : {}({})'.format(str * abs(avgGap), avgGap))

