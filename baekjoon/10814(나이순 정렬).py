import sys
input = sys.stdin.readline

n = int(input())
users = [list(map(str, input().split())) for _ in range(n)]

users.sort(key = lambda x: int(x[0]))

for i in users:
  print(*i)