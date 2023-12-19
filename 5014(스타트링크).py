from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0] * (1000001)

queue = deque([s])

while queue:
  x = queue.popleft()

  if x == g:
    print(visited[x])
    break

  for i in (x+u, x-d):
    if i == x:
      continue
    if 0 < i <= f and visited[i] == 0:
      visited[i] = visited[x] + 1
      queue.append(i)

else:
  print("use the stairs")



  