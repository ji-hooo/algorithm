import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0

while a:
  res += (a.pop(a.index(min(a))) * b.pop(b.index(max(b))))

print(res)