import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time = 99999999
height = 0

for i in range(257):
  maxTime, minTime = 0, 0

  for j in range(n):
    for k in range(m):
      if board[j][k] >= i:
        maxTime += board[j][k] - i
      else:
        minTime += i - board[j][k]
    
  if minTime <= maxTime + b:
    if minTime + (maxTime * 2) <= time:
      time = minTime + (maxTime * 2)
      height = i

print(time, height)