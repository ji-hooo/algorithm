import sys

length = int(input())

for i in range(length):
  x, y = map(int, sys.stdin.readline().split())
  print(x + y)