def makeTeam(votes, N):
	isGroupMember = [False] * (N + 1)

	for i, j in votes:
		# False, False
		if (not isGroupMember[i]) and (not isGroupMember[j]):
			isGroupMember[i], isGroupMember[j] = i, i #i를 집합의 대표로 설정하고, 그것을 isGroupMember에 표시
		#True, False
		elif isGroupMember[i] and (not isGroupMember[j]):
			isGroupMember[j] = isGroupMember[i] #i의 대표 노드를 j도 가지도록 설정
		#False, True
		elif (not isGroupMember[i]) and isGroupMember[j]:
			isGroupMember[i] = isGroupMember[j]
		#True, True
		else:
			representative_node = isGroupMember[i]
			opposite_node = isGroupMember[j]
			isGroupMember = [representative_node if _ == opposite_node else _ for _ in isGroupMember]

	isGroupMember = [ -_ if not isGroupMember[_] else isGroupMember[_] for _ in range(len(isGroupMember))]

	return len(set(isGroupMember[1:]))



T = int(input())

for test_case in range(1, T+1):
	N, M =list(map(int, input().split()))

	lists = list(map(int, input().split()))

	votes = [(lists[_], lists[_+1]) for _ in range(0, len(lists), 2)]

	print(f"#{test_case} {makeTeam(votes, N)}")

'''
Test Case

1
8 4
1 2 3 4 5 6 1 6
answer = 4
'''