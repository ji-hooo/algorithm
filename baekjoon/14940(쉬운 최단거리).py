import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
visit = [[False] * m for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
q = deque([])

for i in range(n):
  line = list(map(int, input().split()))

  for j in range(m):
    if line[j] == 2:
      q.append((i, j))
      visit[i][j] = True
      distance[i][j] = 0
    
    if line[j] == 0:
      distance[i][j] = 0
    
  board.append(line)

x_direction = [-1, 1, 0, 0]
y_direction = [0, 0, -1, 1]

while q:
  x, y = q.popleft()

  for i in range(4):
    nx, ny = x + x_direction[i], y + y_direction[i]

    if 0 <= nx < n and 0 <= ny < m:
      if not visit[nx][ny] and board[nx][ny] == 1:
        q.append((nx, ny))
        visit[nx][ny] = True
        distance[nx][ny] = distance[x][y] + 1

for row in distance:
  for i in row:
    print(i, end=" ")
  print()