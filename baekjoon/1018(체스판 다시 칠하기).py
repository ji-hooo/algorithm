import sys
input = sys.stdin.readline

board = []

n, m = map(int, input().split())

for i in range(n):
  board.extend([input().rstrip()])

min_count = 32

for i in range(n-7):
  for j in range(m-7):
    count = 0
    for k in range(i, i + 8):
      for l in range(j, j + 8):
        if ((k + l) % 2 == 0 and board[k][l] == "B") or ((k + l) % 2 == 1 and board[k][l] == "W"):
          count += 1
    min_count = min(count, 64 - count, min_count)

print(min_count)