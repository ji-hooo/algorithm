import sys
input = sys.stdin.readline

n = int(input())
ns = set(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

for m in ms:
  if (m in ns):
    print(1)
  else:
    print(0)