import sys
input = sys.stdin.readline

n = int(input())

row = list(map(int, input().split()))

length = [0] * n

for i in range(n):
  for j in range(i):
    if row[j] < row[i] and length[i] < length[j]:
      length[i] = length[j]
  
  length[i] += 1

print(max(length))