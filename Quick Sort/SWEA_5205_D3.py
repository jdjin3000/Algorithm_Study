def partition(lists):
	len_ = len(lists)
	if len_ <= 1:
		return lists

	pivot = lists[0]
	lower_line = 1
	upper_line = len_ - 1

	while True:
		if lists[lower_line] > pivot:
			if lists[upper_line] < pivot:
				lists[lower_line], lists[upper_line] = lists[upper_line], lists[lower_line]
			else:
				upper_line -= 1
		else:
			lower_line += 1

		if lower_line > upper_line:
			lists[0], lists[upper_line] = lists[upper_line], lists[0]
			break

	left_list, right_list = lists[:upper_line], lists[upper_line+1:]
	sorted_left_list = partition(left_list)
	sorted_right_list = partition(right_list)

	return sorted_left_list + [pivot] + sorted_right_list

T = int(input())

for test_case in range(1, T+1):
	N = int(input())
	lists = list(map(int, input().split()))

	print(f"#{test_case} {partition(lists)[N//2]}")