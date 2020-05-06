N = int(input())
maps =[list(map(int, list(input()))) for i in range(N)]

#접근을 했는지 파악하는 List. maps[j][k] 접근 -> dpMaps[j][k] = True
dpMaps =[[False for j in range(N)] for i in range(N)]
Queue = []
countList = []
count = 0

#maps 순회
for i in range(N):
	for j in range(N):
		#순회 중, 1 조우.
		if maps[i][j] == 1:
			#BFS를 위한 Queue 삽입(First Node)
			Queue.append((i, j))

			while Queue:
				#Queue 맨 앞의 노드 pop
				n, m = Queue.pop(0)
				dpMaps[n][m] = True
				#maps 순회 시 이미 조회한 곳은 걸리지 않도록 하기 위하여 0으로 변환
				maps[n][m] = 0

				#노드의 갯수 파악.
				count += 1

				#현재 위치에서의 자식 노드 파악.
				#자식 노드의 기준.
				#1. 현재 맵 위치 상에서 맨하탄 거리로 1만 차이날 것.
				#2. 값이 1일 것.
				#3. 이미 다른 노드의 자식 노드로서 Queue에 들어가지 않았을 것. (dpMaps로 확인)
				childNode = [(n+1, m), (n, m+1), (n-1, m), (n, m-1)]
				childNode = [ cn for cn in childNode if max(cn) < N and min(cn) >= 0 and maps[cn[0]][cn[1]] == 1 and dpMaps[cn[0]][cn[1]] is False]

				#트리가 아니므로 자식 노드가 중첩될 가능성이 있기 때문에 True로 설정하여 방지.
				for x, y in childNode:
					dpMaps[x][y] = True

				#해당 위치에서의 자식 노드 큐 삽입.
				Queue += childNode

			#정답 출력을 위해 노드의 갯수를 기록한다.
			countList.append(count)
			#다음 순회를 위해 초기화
			count = 0

print(len(countList))
for i in sorted(countList):
	print(i)