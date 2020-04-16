def solution(bridge_length, weight, truck_weights):
	time = 0
	sumOfTruckWeights = 0
	bridge = []
	while truck_weights != [] or bridge != []:
		time += 1

		bridge = [(i[0], i[1] + 1) for i in bridge if i[1] + 1 <= bridge_length]

		weightUpdate = list(map(sum, zip(*bridge)))
		if weightUpdate:
			sumOfTruckWeights = weightUpdate[0]
		else:
			sumOfTruckWeights = 0

		if truck_weights != [] and truck_weights[0] + sumOfTruckWeights <= weight:
			bridge.append((truck_weights[0], 1))
			del truck_weights[0]

	answer = time
	return answer