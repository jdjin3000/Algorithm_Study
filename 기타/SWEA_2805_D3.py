T = int(input())
for test_case in range(1, T + 1):
	N = int(input())
	mid = N//2
	sums = 0
	lists = []

	for i in range(N):
		lists.append(list(map(int, list(input()))))

	sums += sum(lists[mid][:])
	for i in range(1, mid+1):
		sums += sum(lists[mid - i][i:N-i])
		sums += sum(lists[mid + i][i:N-i])
	
	print('#' + str(test_case) + ' ' + str(sums))
	del lists[:]