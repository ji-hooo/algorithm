import sys
input = sys.stdin.readline

n = int(input())

name = 666
series_num = 1

while series_num < n:
  name += 1
  if "666" in str(name):
    series_num += 1

print(name)