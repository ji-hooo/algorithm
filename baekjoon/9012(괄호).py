import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
  content = input().rstrip()
  while '()' in content:
    content = content.replace('()', '')
  print('NO' if content else 'YES')