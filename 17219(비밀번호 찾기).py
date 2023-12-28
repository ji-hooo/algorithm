import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}

for _ in range(n):
  site, password = map(str, input().split())
  memo[site] = password

for _ in range(m):
  search_site = str(input().rstrip())
  print(memo[search_site])