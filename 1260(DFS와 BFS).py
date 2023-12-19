import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

for i in range(n+1):
  graph[i].sort()

def dfs(v):
  visited[v] = True
  print(v, end = ' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):
  queue = deque([v])
  visited[v] = True

  while queue:
    v = queue.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


visited = [False] * (n+1)
dfs(v)

print()
visited = [False] * (n+1)
bfs(v)