import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in (range(t)):
  n, target = map(int, input().split())
  priorities = deque(list(map(int, input().split())))
  count = 0

  while priorities:
    if max(priorities) == priorities[0]:
      if (target == 0):
        print(count + 1)
        break

      else:
        priorities.popleft()
        count += 1
        target -= 1

    else:
      priorities.append(priorities.popleft())
      target = (len(priorities) - 1 if target == 0 else target - 1)