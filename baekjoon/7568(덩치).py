import sys
input = sys.stdin.readline


n = int(input())
big = [list(map(int, input().split())) for _ in range(n)]
ranking = [1] * n

for i in range(n):
  for j in range(n):
    if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
      ranking[i] += 1

print(*ranking)
