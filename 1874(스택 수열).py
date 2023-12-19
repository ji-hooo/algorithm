import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input().rstrip()) for _ in range(n)]

signs = []
stack = []
num = 1

for i in arr:
  while num <= i:
    stack.append(num)
    signs.append("+")
    num += 1
  
  if stack and stack[-1] == i:
    stack.pop()
    signs.append("-")
  else:
    print("NO")
    break

else:
  for sign in signs:
    print(sign)