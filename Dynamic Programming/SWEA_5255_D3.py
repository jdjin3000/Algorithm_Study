def tile_DP(N):
	global optimized_list
	if optimized_list[N]:
		return optimized_list[N]

	optimized_list[N] = tile_DP(N-1) * 1 + tile_DP(N-2) * 2 + tile_DP(N-3) * 1

	return optimized_list[N]

T = int(input())

for test_case in range(1, T+1):
	N = int(input())
	optimized_list = [False] * (N + 1)
	optimized_list[0] = 0
	optimized_list[1] = 1
	optimized_list[2] = 3
	optimized_list[3] = 6

	print(f"#{test_case} {tile_DP(N)}")