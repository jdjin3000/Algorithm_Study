def walk(lists, trial, m, n):
	for x, y in trial:
		if not (-1 < x < n and -1 < y < m) or lists[x][y] == -1:
			continue

		if x == 0: # and y <= m - 1
			if lists[x][y-1] != -1:
				lists[x][y] += lists[x][y-1]
		elif y == 0: # and x <= n - 1
			if lists[x-1][y] != -1:
				lists[x][y] += lists[x-1][y]
		elif 0 < x <= n - 1 and 0 < y <= m - 1:
			left_value = lists[x][y-1]
			up_value = lists[x-1][y]

			if left_value == -1:
				left_value = 0
			if up_value == -1:
				up_value = 0
			
			lists[x][y] = left_value + up_value

	return lists


def solution(m, n, puddles):
	lists = [[0 for j in range(m)] for i in range(n)]
	
	for i, j in puddles:
		lists[j - 1][i - 1] = -1 # puddle, 문제는 좌표 (1, 1) 부터 시작, m이 열의 수, n이 행의 수

	if lists[1][0] != -1:
		lists[1][0] = 1
	if lists[0][1] != -1:
		lists[0][1] = 1

	for step in range(1, m + n - 1): #(0, 0)은 제외
		trial = [(_, step - _) for _ in range(step+1)]
		lists = walk(lists, trial, m, n)

	return lists[-1][-1] % 1000000007