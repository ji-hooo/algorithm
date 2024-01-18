import sys
from collections import deque

input = sys.stdin.readline
# 재귀 깊이 제한 설정
sys.setrecursionlimit(10 ** 6)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 그래프 그리기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 정점 번호 정렬
for i in range(n+1):
  graph[i].sort()

def dfs(v):
  # 정점 방문 처리
  visited[v] = 1
  print(v, end = ' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(i)

def bfs(v):
  q = deque([v])
  #정점 방문 처리
  visited[v] = 1

  while q:
    v = q.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1


visited = [0] * (n+1)
dfs(v)

print()
visited = [0] * (n+1)
bfs(v)