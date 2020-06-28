INF = 10**3

def Prim(Adjacency_Matrix, num_node):
	visited = [False] * num_node
	distance = [INF] * num_node

	#'노드 번호 0' 부터 시작
	distance[0] = 0

	for i in range(num_node):
		selected_node = -1 #아무 노드도 선택되지 않은 상태
		for _ in range(num_node):
			#1. 한번도 방문 하지 않았어야 함. (필수조건)
			#2. 아무 노드도 선택되지 않은 상태  or  현재 선택된 노드보다 거리가 짧을 때
			if not visited[_] and (selected_node == -1 or distance[_] < distance[selected_node]):
				selected_node = _

		visited[selected_node] = True

		for _ in range(num_node):
			if not visited[_] and Adjacency_Matrix[selected_node][_] < distance[_]:
				distance[_] = Adjacency_Matrix[selected_node][_]

	return sum(distance)


T = int(input())

for test_case in range(1, T+1):
	V, E = map(int,input().split())
	#노드 번호는 0, 1, 2 ... 로 붙는다. 즉 V == 2이면 노드는 3개다.
	Edge = [list(map(int,input().split())) for _ in range(E)]

	#인접행렬 제작
	adjacency_matrix = [[0 if i==j else INF for j in range(V+1)] for i in range(V+1)]
	for i, j, weight in Edge:
		adjacency_matrix[i][j], adjacency_matrix[j][i] = weight, weight #무방향 그래프이기 때문에 양방향 모두 같은 가중치를 지닌다.

	print(f"#{test_case} {Prim(adjacency_matrix, V+1)}")