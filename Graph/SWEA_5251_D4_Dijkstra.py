from collections import deque
INF = 10**3

def dijkstra(Adjacency_Matrix, num_node):
	visited = [False] * num_node
	distance = [0] + [INF] * (num_node - 1) #0번 노드의 거리는 0

	Queue = deque()
	Queue.append(0)

	while Queue:
		selected_node = Queue.popleft()
		visited[selected_node] = True
		
		for _ in range(num_node):
			if not visited[_] and not Adjacency_Matrix[selected_node][_] in [0, INF]:
				Queue.append(_)
				updated_cost = distance[selected_node] + Adjacency_Matrix[selected_node][_]
				if updated_cost < distance[_]:
					distance[_] = updated_cost

	return distance[-1] # N번 노드에 도달하는데 소모되는 비용




T = int(input())

for test_case in range(1, T+1):
	N, E = map(int, input().split())

	Edge = [list(map(int, input().split())) for _ in range(E)]

	#인접행렬
	adjacency_matrix = [[0 if i==j else INF for j in range(N+1)] for i in range(N+1)]
	for i, j, weight in Edge:
		adjacency_matrix[i][j] = weight

	print(f"#{test_case} {dijkstra(adjacency_matrix, N+1)}")