import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if m != 0:
  broken = list(map(int, input().split()))
else:
  broken = []

if n == 100:
  print(0)

else:
  count = abs(100 - n)

  for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
      if int(i[j]) in broken:
        break
        
      if j == len(i) - 1:
        count = min(count, abs(int(i) - n) + len(i))

  print(count)