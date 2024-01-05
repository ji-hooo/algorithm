import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = [0] * (n + 1)

for _ in range(n - 1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

def bfs(tree, v, visited):
  q = deque([v])
  visited[v] = True
  while q:
    x = q.popleft()
    for i in tree[x]:
      if not visited[i]:
        ans[i] = x
        q.append(i)
        visited[i] = True

bfs(tree, 1, visited)

for i in range(2, n + 1):
  print(ans[i])