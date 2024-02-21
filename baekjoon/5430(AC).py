import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  funcs = input().rstrip()
  
  n = int(input())
  if n == 0:
    input()
    numlist = deque([])
  else:
    numlist = deque(list(input().strip("[]\n").split(",")))

  front = True
  for func in funcs:
    if func == 'R':
      if front:
        front = False
      else:
        front = True
    else:
      if numlist:
        if front:
          numlist.popleft()
        else:
          numlist.pop()
      else:
        print("error")
        break

  else:
    if front:
      print('[' + ','.join(numlist) + ']')
    else:
      numlist.reverse()
      print('[' + ','.join(numlist) + ']')
