import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  k = int(input())
  minHeap = []
  maxHeap = []
  visited = [0] * k

  for i in range(k):
    alpha, num = map(str, input().split())
    num = int(num)

    if alpha == 'I':
      heapq.heappush(minHeap, (num, i))
      heapq.heappush(maxHeap, (-num, i))
    elif alpha == 'D' and num == 1 and maxHeap:
      visited[heapq.heappop(maxHeap)[1]] = 1
    elif alpha == 'D' and num == -1 and minHeap:
      visited[heapq.heappop(minHeap)[1]] = 1

    while minHeap and visited[minHeap[0][1]]:
      heapq.heappop(minHeap)
    while maxHeap and visited[maxHeap[0][1]]:
      heapq.heappop(maxHeap)

  if maxHeap:
    print(-maxHeap[0][0], minHeap[0][0])
  else:
    print('EMPTY')