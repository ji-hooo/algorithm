import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bundles = []
piece = []
res = 0

for _ in range(m):
  six, one = map(int, input().split())
  bundles.append(six)
  piece.append(one)

if min(piece) * 6 >= min(bundles):
  res += min(bundles) * (n // 6)
  n %= 6

  if min(bundles) <= (n * min(piece)):
    res += min(bundles)
    n = 0

res += min(piece) * n

print(res)
