import sys
input = sys.stdin.readline

n, k = map(int, input().split())

person = [i + 1 for i in range(n)]
res = []
idx = 0

while person:
  idx += k - 1
  if idx >= len(person):
    idx %= len(person)
  res.append(str(person.pop(idx)))

print('<', ', '.join(res), '>', sep='')