import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))
location1, location2 = map(int, input().split())


def di(location1):
  distance[location1] = 0
  heap = []
  heapq.heappush(heap, (0, location1))

  while heap:
    weight, now = heapq.heappop(heap)

    if distance[now] < weight:
      continue

    for node in graph[now]:
      c = weight + node[1]
      if c < distance[node[0]]:
        distance[node[0]] = c
        heapq.heappush(heap, (c, node[0]))

di(location1)

print(distance[location2])