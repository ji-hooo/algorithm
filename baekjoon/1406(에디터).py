import sys
input = sys.stdin.readline

command_l = list(input().rstrip())
command_r = []

for i in range(int(input())):
  order = list(map(str, input().split()))

  if order[0] == 'P':
    command_l.append(order[1])

  elif order[0] == 'L':
    if command_l:
      command_r.append(command_l.pop())
  
  elif order[0] == 'D':
    if command_r:
      command_l.append(command_r.pop())

  elif order[0] == 'B':
    if command_l:
      command_l.pop()

print(''.join(command_l) + ''.join(command_r[::-1]))