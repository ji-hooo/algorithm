import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
  q = deque([v])
  visit[v] = 1

  while q:
    tmp = q.popleft()
    for i in graph[tmp]:
      if visit[i] == 0:
        visit[i] = visit[tmp] + 1
        q.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

bacon = []

for i in range(1, n + 1):
  visit = [0] * (n + 1)
  if visit[i] == 0:
    bfs(i)
    bacon.append(sum(visit))

print(bacon.index(min(bacon)) + 1)