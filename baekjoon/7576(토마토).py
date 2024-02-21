import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for x in range(n):
  for y in range(m):
    if board[x][y] == 1:
      q.append((x, y))

def BFS():
  count = 0

  dxdy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  while q:
    x, y = q.popleft()
    for dx, dy in dxdy:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
        board[nx][ny] = board[x][y] + 1
        q.append((nx, ny))
  
  for i in board:
    if 0 in i:
      print(-1)
      exit()
    else:
      count = max(count, max(i))
  
  print(count - 1)

BFS()

