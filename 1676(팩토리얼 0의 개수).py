import sys
input = sys.stdin.readline

n = int(input())

m = 1
count = 0

for i in range(2, n + 1):
  m *= i

m = str(m)

for i in range(1, len(m) + 1):
  if int(m[-i]) != 0:
    break
  else:
    count += 1

print(count)