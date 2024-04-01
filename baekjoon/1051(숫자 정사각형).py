import sys
input = sys.stdin.readline

n, m = map(int, input().split())
squre = [list(map(int, input().rstrip())) for _ in range(n)]

size = min(n, m)
result = []

for i in range(n):
  for j in range(m):
    for k in range(size):
      if ((i + k) < n) and ((j + k) < m):
        if (squre[i][j] == squre[i + k][j] == squre[i][j + k] == squre[i + k][j + k]):
          result.append((k + 1) ** 2)

print(max(result))