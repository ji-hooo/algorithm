import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [[0] * (n + 1)]
for i in range(n):
  row = list(map(int, input().split()))
  board.append([0] + row)

sum_board = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    sum_board[i][j] = board[i][j] + sum_board[i - 1][j] + sum_board[i][j - 1] - sum_board[i - 1][j - 1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(sum_board[x2][y2] - sum_board[x1 - 1][y2] - sum_board[x2][y1 - 1] + sum_board[x1 - 1][y1 - 1])