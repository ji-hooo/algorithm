import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
q = deque(range(1, n + 1))
nums = list(map(int, input().split()))
count = 0

for num in nums:
  while q:
    if q[0] == num:
      q.popleft()
      break
    
    if q.index(num) <= len(q) // 2:
      q.append(q.popleft())
    else:
      q.appendleft(q.pop())

    count += 1

print(count)
