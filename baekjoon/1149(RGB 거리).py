import sys
input = sys.stdin.readline

n = int(input())

money = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  money[i][0] += min(money[i - 1][1], money[i - 1][2])
  money[i][1] += min(money[i - 1][0], money[i - 1][2])
  money[i][2] += min(money[i - 1][0], money[i - 1][1])

print(min(money[-1]))