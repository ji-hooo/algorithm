import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input().rstrip()) for _ in range(n)]

count = 0
for i in range(n - 1, -1, -1):
  if k == 0:
    break
  if k >= coins[i]:
    count += (k // coins[i])
    k %= coins[i]

print(count)