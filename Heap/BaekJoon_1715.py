import heapq
N = int(input())

heap = []
answer = 0

for i in range(N):
	heapq.heappush(heap, int(input()))

while len(heap) != 1:
	temp = heapq.heappop(heap) + heapq.heappop(heap)
	heapq.heappush(heap, temp)
	answer += temp

print(answer)