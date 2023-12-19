import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def bfs(x, y):
  x_loc = [-1, 1, 0, 0]
  y_loc = [0, 0, -1, 1]
  for i in range(4):
    nx, ny = x + x_loc[i], y + y_loc[i]
    if (0 <= nx <= n-1) and (0 <= ny <= m-1):
      if board[nx][ny] == 1:
        board[nx][ny] = 0
        bfs(nx, ny)

t = int(input())

for i in range(t):
  m, n, k = map(int, input().split())
  board = [[0 for _ in range(m)] for _ in range(n)]
  count = 0

  for j in range(k):
    y, x = map(int, input().split())
    board[x][y] = 1

  for o in range(n):
    for p in range(m):
      if board[o][p] == 1:
        bfs(o, p)
        count += 1
      else:
        continue 

  print(count)