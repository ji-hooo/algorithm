import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


q = deque()
result = []

def bfs(y, x):
  if board[y][x] == 1:
    board[y][x] = 0
    q.append((y, x))
    count = 0
    while q:
      count += 1
      y, x = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
          if board[ny][nx] == 1:
            q.append((ny, nx))
            board[ny][nx] = 0
    result.append(count)

for y in range(n):
  for x in range(n):
    bfs(y, x)

result.sort()
print(len(result))
for i in result:
  print(i)