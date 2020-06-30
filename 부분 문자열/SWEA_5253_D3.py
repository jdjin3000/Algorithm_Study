def checkPrefix(A_list, B_list):
	answer = 0

	for B in B_list:
		for A in A_list:
			if A[:len(B)] == B:
				answer += 1
				break

	return answer

T = int(input())

for test_case in range(1, T+1):
	A, B = map(int, input().split())
	A_list = [input() for _ in range(A)]
	B_list = [input() for _ in range(B)]

	print(f"#{test_case} {checkPrefix(A_list, B_list)}")