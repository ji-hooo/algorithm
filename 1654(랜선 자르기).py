import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lans = [int(input()) for _ in range(k)]

start, end = 1, sum(lans)

while start <= end:
  mid = (start + end) // 2
  lines = 0

  for i in lans:
    lines += i // mid

  if lines >= n:
    start = mid + 1
  else:
    end = mid - 1

print(end)
    