T = int(input())
for test_case in range(1, T + 1):
	N, M, L = list(map(int, input().split()))
	Tree = [-1 for i in range(N + 1)]
	leafs = []
	for i in range(M):
		leafs.append(list(map(int, input().split())))

	leafs.sort()

	for i in range(M):
		Tree[N+1-M + i] = leafs[i][1]

	for i in range(N, 0, -1):
		if i%2 == 1:
			Tree[i//2] = Tree[i] + Tree[i-1]
		elif Tree[i//2] == -1:
			Tree[i//2] = Tree[i]

	print('#'+str(test_case)+' '+ str(Tree[L]))
