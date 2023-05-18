import operator
passScore1= 60
passScore2= 70

korScore=int(input('국어 점수:'))
engScore=int(input('영어 점수:'))
matScore = int(input('수학 점수 :'))

totalScore = korScore + engScore+matScore
scoreAvg = totalScore/3

print('국어 : PASS') if operator.ge(korScore, passScore1) else print('국어 : FAIL')
print('영어 : PASS') if operator.ge(engScore, passScore1) else print('영어 : FAIL')
print('수학 : PASS') if operator.ge(matScore, passScore1) else print('수학 : FAIL')
print('시험 : PASS') if operator.ge(scoreAvg, passScore2) else print('시험 : FAIL')

print('총 점 : %d, 평균 : %.2f' % (totalScore, scoreAvg))