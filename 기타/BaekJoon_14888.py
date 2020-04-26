from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
op = ['+', '-', '*', '/']
opNums = list(map(int, input().split()))

operators = [op[i] for i in range(4) for j in range(opNums[i])]

operationList = set(permutations(operators, len(operators)))

result = []

for ops in operationList:
	temp = nums[0]
	for i in range(0, N-1):
		if ops[i] == '+':
			temp += nums[i+1]
		elif ops[i] == '-':
			temp -= nums[i+1]
		elif ops[i] == '*':
			temp *= nums[i+1]
		elif ops[i] == '/':
			temp /= nums[i+1]
			temp = int(temp)

	result.append(temp)
		
print(max(result))
print(min(result))