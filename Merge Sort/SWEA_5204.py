#강좌의 병합정렬로 풀면 시간초과 오류가 난다고 한다...
#https://swexpertacademy.com/main/help/report/reportBoardView.do?commuId=AWzwjjgqvT4DFARQ

def divide(list_):
	N = len(list_)

	if N <= 1:
		return list_, 0

	left = list_[:N//2]
	right = list_[N//2:]

	left_, count_left = divide(left)
	right_, count_right = divide(right)

	result, count = merge(left_, right_)

	count += count_left + count_right

	return result, count

def merge(left, right):
	result = []
	count = 0

	if left[-1] > right[-1]:
		count += 1

	while len(left) or len(right):
		if len(left) and len(right):
			if left[0] < right[0]:
				result.append(left[0])
				del left[0]
			else:
				result.append(right[0])
				del right[0]
		elif len(left):
			result.append(left[0])
			del left[0]
		else:
			result.append(right[0])
			del right[0]

	return result, count

T = int(input())

for test_case in range(1, T + 1):
	N = int(input())
	result1, count = divide(list(map(int, input().split())))

	print(f"#{test_case} {result1[N//2]} {count}")