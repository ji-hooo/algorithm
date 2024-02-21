import sys
input = sys.stdin.readline

deq = []

for _ in range(int(input())):
  commands = list(map(str, input().split()))

  if commands[0] == 'push_front':
    deq.insert(0, int(commands[1]))
  
  elif commands[0] == 'push_back':
    deq.append(commands[1])

  elif commands[0] == 'pop_front':
    if len(deq) == 0:
      print(-1)
      continue
    else:
      print(deq[0])
      del(deq[0])

  elif commands[0] == 'pop_back':
    if len(deq) == 0:
      print(-1)
      continue
    else:
      print(deq[-1])
      del(deq[-1])

  elif commands[0] == 'size':
    print(len(deq))

  elif commands[0] == 'empty':
    print(0 if deq else 1)

  elif commands[0] == 'front':
    print(deq[0] if len(deq) else -1)

  else:
    print(deq[-1] if len(deq) else -1)