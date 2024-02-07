import sys
input = sys.stdin.readline

k = int(input())
summ = []

for _ in range(k):
  n = int(input())
  if n == 0:
    summ.pop()
  else:
    summ.append(n)
  
print(sum(summ))