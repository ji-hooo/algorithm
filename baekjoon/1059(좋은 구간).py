import sys
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()

if n in s:
  print(0)

else:
  min, max = 0, 0
  for num in s:
    if num < n:
      min = num + 1
    elif num > n and max == 0:
      max = num - 1

  res = (n - min) * (max - n + 1) + (max - n)

  print(res) 