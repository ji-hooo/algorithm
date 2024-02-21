import sys
input = sys.stdin.readline

def round(n):
  if n - int(n) >= 0.5:
    return int(n) + 1
  else:
    return int(n)

n = int(input())

if n == 0:
  print(0)
else:
  opinions = [int(input()) for _ in range(n)]
  opinions.sort()

  start_idx = round(n * 0.15)

  score = opinions[start_idx : n - start_idx]

  print(round(sum(score) / len(score)))

