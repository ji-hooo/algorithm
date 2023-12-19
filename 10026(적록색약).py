import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)]
visited = [[False] * (n + 1) for _ in range(n + 1)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()
count = 0

def bfs(x,y):
  global count
  q.append([x,y])
  visited[x][y] = True
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
        if board[x][y] == board[nx][ny]:
          visited[nx][ny] = True
          q.append([nx,ny])
        
    
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(i, j)
      count += 1

print(count, end = " ")

for i in range(n):
  for j in range(n):
    if board[i][j] == "R":
      board[i][j] = "G"

visited = [[False] * (n + 1) for _ in range(n + 1)]
count = 0

for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(i, j)
      count += 1
      
print(count)