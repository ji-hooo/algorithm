import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

location = [0] * (100001)

q = deque()
q.append(n)

def bfs(k):

  while q:
    n = q.popleft()
    move = [n - 1, n + 1, n * 2]

    if n == k:
      print(location[n])
      break
    
    for i in move:
      if (0 <= i <= 100000) and location[i] == 0:
        location[i] = location[n] + 1
        q.append(i)

bfs(k)