import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [0] * (n + 1)
visited[1] = 1
graph = [[] for _ in range(n + 1)]
count = 0

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(start):
  global count
  for i in graph[start]:
    if visited[i] == 0:
      visited[i] = 1
      count += 1
      dfs(i)

dfs(1)

print(count)



