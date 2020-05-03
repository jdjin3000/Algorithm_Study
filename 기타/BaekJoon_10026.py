import sys
sys.setrecursionlimit(100000)

N = int(input())

maps = [list(input()) for i in range(N)]
RGmaps =[[char if char=='B' else 'R' for char in line] for line in maps]

def findArea(maps, pos, startingColor, N):
	maps[pos[0]][pos[1]] = 0

	moves = [(pos[0]+1, pos[1]), (pos[0], pos[1]+1), (pos[0]-1, pos[1]), (pos[0], pos[1]-1)]
	moves = [i for i in moves if max(i)<N and min(i)>=0]

	for mv in moves:
		i, j = mv
		if maps[i][j] == startingColor:
			maps = findArea(maps, mv, startingColor, N)

	return maps

def searchMap(maps, N):
	result = 0

	for i in range(N):
		for j in range(N):
			if maps[i][j] != 0:
				result += 1
				maps = findArea(maps, (i, j), maps[i][j], N)

	return result

print(searchMap(maps, N), end=' ')
print(searchMap(RGmaps, N))