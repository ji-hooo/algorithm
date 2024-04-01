import sys

input = sys.stdin.readline

n, l = map(int, input().split())

taped, count = 0, 0

leaks = sorted(list(map(int, input().split())))

for i in leaks:
  if i > taped:
    count += 1
    taped = i + l - 1

print(count)