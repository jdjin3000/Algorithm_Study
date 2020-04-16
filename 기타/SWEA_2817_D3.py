from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
	sums = 0

	N, K = list(map(int,input().split()))
	lists = list(map(int, input().split()))

	sums = lists.count(K)

	for i in range(2, N + 1, 1):
		combi = combinations(lists,i)
		lists2 = list(map(sum, combi))
		sums += lists2.count(K)

	print('#' + str(test_case) + ' ' + str(sums))
	del lists[:]