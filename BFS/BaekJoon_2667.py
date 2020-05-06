N = int(input())
maps =[list(map(int, list(input()))) for i in range(N)]
dpMaps =[[False for j in range(N)] for i in range(N)]
Queue = []
countList = []
count = 0

for i in range(N):
	for j in range(N):
		if maps[i][j] == 1:
			Queue.append((i, j))

			while Queue:
				n, m = Queue.pop(0)
				dpMaps[n][m] = True
				maps[n][m] = 0
				count += 1

				childNode = [(n+1, m), (n, m+1), (n-1, m), (n, m-1)]
				childNode = [ cn for cn in childNode if max(cn) < N and min(cn) >= 0 and maps[cn[0]][cn[1]] == 1 and dpMaps[cn[0]][cn[1]] is False]

				for x, y in childNode:
					dpMaps[x][y] = True

				Queue += childNode


			countList.append(count)
			count = 0

print(len(countList))
for i in sorted(countList):
	print(i)