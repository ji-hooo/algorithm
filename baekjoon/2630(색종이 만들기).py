import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def divide(x, y, n):
  a = same(x, y, n)
  if a == 2:
    divide(x, y, n // 2)
    divide(x + n // 2, y, n // 2)
    divide(x, y + n // 2, n // 2)
    divide(x + n // 2, y + n // 2, n // 2)
  elif a == 1:
    global blue
    blue += 1
  elif a == 0:
    global white
    white += 1


def same(x, y, n):
  sum = 0
  for i in range(x, x + n):
    for j in range(y, y + n):
      sum += paper[i][j]
  
  if sum == 0:
    return 0
  elif sum == n ** 2:
    return 1
  else:
    return 2

divide(0, 0, n)
print(white)
print(blue)