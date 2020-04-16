T = int(input())

for test_case in range(1, T + 1):
	N, M = map(int, input().split())
	used = set()
	lists = []
	for i in range(M):
		m1, m2 = map(int, input().split())
		used.add(m1)
		used.add(m2)
		lists.append({m1, m2})

	used = list(used)

	if len(used) != N:
		for i in range(1,N+1):
			if not i in used:
				lists.append({i})

	while sum(len(elements) for elements in lists) != N:
		for i in range(len(lists) - 1):
			for j in range(i+1, len(lists), 1):
				if len(lists[i] & lists[j]) is not 0:
					lists[i] = lists[i] | lists[j]
					del lists[j]
					break

	print(lists)
	print('#' + str(test_case) + ' ' + str(len(lists)))

	del lists[:]
