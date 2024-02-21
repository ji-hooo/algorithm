import sys
input = sys.stdin.readline

q = []

for _ in range(int(input())):
  commands = list(map(str, input().split()))

  if commands[0] == 'push':
    q.append(int(commands[1]))

  elif commands[0] == 'pop':
    if len(q) == 0:
      print(-1)
      continue
    else:
      print(q[0])
      del(q[0])

  elif commands[0] == 'size':
    print(len(q))

  elif commands[0] == 'empty':
    print(0 if q else 1)

  elif commands[0] == 'front':
    print(q[0] if len(q) else -1)

  else:
    print(q[-1] if len(q) else -1)