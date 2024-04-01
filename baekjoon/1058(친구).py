import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    for k in range(n):
      if j == k:
        continue
      if graph[j][k] == 'Y':
        visited[j][k] = True
      if graph[j][i] == 'Y' and graph[i][k] == 'Y':
        visited[j][k] = True

result = 0
for i in range(n):
  result = max(sum(visited[i]), result)

print(result)