import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = []

def dfs(a):
  if len(visited) == m:
    print(*visited)

  for i in range(a, n + 1):
    if i not in visited:
      visited.append(i)
      dfs(i + 1)
      visited.pop()

dfs(1)