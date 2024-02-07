import sys
input = sys.stdin.readline

n = int(input())

sugarBag = 0

while n >= 0:
  if n % 5 == 0:
    sugarBag += (n // 5)
    print(sugarBag)
    break
  n -= 3
  sugarBag += 1

else:
  print(-1)