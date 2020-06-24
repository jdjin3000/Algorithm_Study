T = int(input())

def backTracking(lists, what_product = 0, factories_in_operation = [], value = 0): #what_product is row index
	global answer

	if value >= answer:
		return
	elif what_product == len(lists):
		answer = value
	else:
		factory_cost = lists[what_product]

		for i in [i for i in range(len(factory_cost)) if i not in factories_in_operation]:
			backTracking(lists, what_product + 1, factories_in_operation + [i], value + factory_cost[i])

	return answer


for test_case in range(1, T+1):
	answer = 10 ** 8
	N = int(input())
	lists = [list(map(int,input().split())) for _ in range(N)]

	print(f"#{test_case} {backTracking(lists)}")