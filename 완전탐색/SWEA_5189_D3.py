from itertools import permutations

T = int(input())

for test_case in range(1, T + 1):
	N = int(input())
	permutation = permutations(range(1, N), N-1)
	scores = []

	vertex = [list(map(int, input().split())) for i in range(N)]
	for scenario in permutation:
		scenario = [0] + list(scenario) + [0] #len(scenario) = N+1

		#vertex[시작위치][도착위치]
		score = sum([vertex[scenario[i-1]][scenario[i]] for i in range(1, len(scenario))])
		scores.append(score)

	print('#'+str(test_case)+' '+str(min(scores)))