import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(n):
  for j in range(m):
    if campus[i][j] == 'I':
      x, y = i, j
      campus[i][j] == 'X'

q = deque([(x, y)])
ans = 0

while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and campus[nx][ny] != 'X':
      if campus[nx][ny] == 'P':
        ans += 1
      campus[nx][ny] = 'X'
      q.append((nx, ny))

print('TT' if ans == 0 else ans)