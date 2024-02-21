import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
  commands = list(map(str, input().split()))

  if commands[0] == 'push':
    stack.append(int(commands[1]))

  elif commands[0] == 'pop':
    if len(stack) == 0:
      print(-1)
      continue
    else:
      print(stack[-1])
      del(stack[-1])

  elif commands[0] == 'size':
    print(len(stack))

  elif commands[0] == 'empty':
    print(0 if stack else 1)

  else:
    print(stack[-1] if len(stack) else -1)