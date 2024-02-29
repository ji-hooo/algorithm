import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
  visited = [False] * 10000
  q = deque()
  q.append((a, ""))
  visited[a] = True

  while q:
    x, y = q.popleft()

    if x == b:
      print(y)
    
    tmp = (x * 2) % 10000
    if not visited[tmp]:
      q.append((tmp, y + "D"))
      visited[tmp] = True
    
    tmp = (x - 1) % 10000
    if not visited[tmp]:
      q.append((tmp, y + "S"))
      visited[tmp] = True

    tmp = (10 * x + (x // 1000)) % 10000
    if not visited[tmp]:
      q.append((tmp, y + "L"))
      visited[tmp] = True
    
    tmp = (x // 10 + (x % 10) * 1000) % 10000
    if not visited[tmp]:
      q.append((tmp, y + "R"))
      visited[tmp] = True

t = int(input())

for _ in range(t):
  a, b = map(int, input().split())
  bfs(a, b)