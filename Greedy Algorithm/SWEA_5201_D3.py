T = int(input())

for test_case in range(1, T+1):
	answer = 0
	num_container, num_truck = map(int,input().split())

	container_weights = sorted(list(map(int, input().split())), reverse = True)
	truck_weights = sorted(list(map(int, input().split())), reverse = True)
	
	for con_w in container_weights:
		if con_w <= truck_weights[0]:
			answer += con_w
			del truck_weights[0]

		if truck_weights == []:
			break

	print(f'#{test_case} {answer}')