#num_change가 -1인 이유는 첫번째 배터리 장착은 변경횟수로 여기지 않기 때문이다.
def backTracking(batteries, remaining_battery=0, Position=0, num_change=-1):
	global best

	if best < num_change:
		return
	elif Position >= len(batteries):
		best = num_change
		return
	else:
		capacity = batteries[Position]
		if remaining_battery >= capacity:
			return
		else:
			num_change += 1
			remaining_battery = capacity

		for i in range(Position + 1, Position + capacity + 1):
			backTracking(batteries, remaining_battery - (i - Position), i, num_change)

		return best

T = int(input())

for test_case in range(1, T+1):
	inputs = list(map(int, input().split()))
	best, batteries = inputs[0]+1, inputs[1:]

	print(f"#{test_case} {backTracking(batteries)}")