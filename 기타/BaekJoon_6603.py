from itertools import combinations

testCase=[]

while True:
	temp = list(map(int, input().split()))
	if len(temp) == 1:
		break
	testCase.append(temp)

for tCase_ in testCase:
	N = tCase_[0]

	for case in list(combinations(tCase_[1:], N)):
		for case_2 in list(combinations(case, 6)):
			print(' '.join(list(map(str,case_2))))
	print()