import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for z in range(h):
  for x in range(n):
    for y in range(m):
      if board[z][x][y] == 1:
        q.append((z, x, y))

def BFS():
  count = 0
  dxdydz = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
  while q:
    z, x, y = q.popleft()
    for dx, dy, dz in dxdydz:
      nx = x + dx
      ny = y + dy
      nz = z + dz
      if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and board[nz][nx][ny] == 0:
        board[nz][nx][ny] = board[z][x][y] + 1
        q.append((nz, nx, ny))
  
  for i in range(h):
    for j in board[i]:
      if 0 in j:
        print(-1)
        exit()
      count = max(count, max(j))
  
  print(count - 1)

BFS()

