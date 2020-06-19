T = int(input())

for test_case in range(1, T+1):
	N = int(input())
	schedule = [list(map(int, input().split())) for i in range(N)]
	schedule.sort(key = lambda x: x[1])

	answer = [schedule[0]]

	for i in range(1, len(schedule)):
		if answer[-1][1] <= schedule[i][0]: #이전 종료 시간 < 이후 시작 시간
			answer.append(schedule[i])

	print('#'+str(test_case)+' '+str(len(answer)))