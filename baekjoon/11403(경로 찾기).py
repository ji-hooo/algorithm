import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(v):
  visited = [0] * n
  q = deque([v])

  while q:
    x = q.popleft()
    for i in range(n):
      if graph[x][i] == 1 and visited[i] == 0:
        q.append(i) 
        visited[i] = 1

  return visited

for i in range(n):
  print(*bfs(i))