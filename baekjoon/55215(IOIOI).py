import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = str(input().rstrip())

res, i, ioi = 0, 0, 0

while i <= m - 2:
  if s[i : i + 3] == 'IOI':
    ioi += 1
    i += 2
    if ioi == n:
      res += 1
      ioi -= 1

  else:
    ioi = 0
    i += 1
  
print(res)