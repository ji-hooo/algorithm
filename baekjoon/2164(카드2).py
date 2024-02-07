import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n + 1)])

while len(q) > 1:
  q.popleft()
  tmp = q.popleft()
  q.append(tmp)

print(*q)