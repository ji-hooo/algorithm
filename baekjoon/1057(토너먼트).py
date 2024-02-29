import sys
input = sys.stdin.readline

n, min, soo = map(int, input().split())

count = 0

while min != soo:
  min -= min // 2
  soo -= soo // 2
  count += 1

print(count)