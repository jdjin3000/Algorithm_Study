import sys
sys.setrecursionlimit(10**9)

N = int(input())
firstMap = [list(map(int, input().split())) for i in range(N)]

MaxHeight = 0
MinHeight = 101

for line in firstMap:
	if MaxHeight < max(line):
		MaxHeight = max(line)
	if MinHeight > min(line):
		MinHeight = min(line)


def findSafeArea(pos, maps, N, rain):
	i, j = pos
	maps[i][j] = -1

	moves =[(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
	moves =[move for move in moves if max(move) < N and min(move) > -1]

	for mv in moves:
		i, j = mv
		if maps[i][j] > rain:
			findSafeArea(mv, maps, N, rain)

def setRain(maps, N, rain):
	numOfSafeArea = 0
	for i in range(N):
		for j in range(N):
			if maps[i][j] > rain:
				numOfSafeArea += 1
				findSafeArea((i, j), maps, N, rain)

	return numOfSafeArea

candidate = []

if MinHeight == MaxHeight:
	print(1)
else:
	for i in range(MinHeight, MaxHeight):
		maps = [list(x) for x in firstMap]
		candidate.append(setRain(maps, N, i))

	print(max(candidate))