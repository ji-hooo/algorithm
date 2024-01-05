import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))

sum = [0] * (n + 1)
temp = 0

for i in range(1, n + 1):
  temp += num[i - 1]
  sum[i] = temp

for _ in range(m):
  a, b = map(int, input().split())
  print(sum[b] - sum[a - 1])