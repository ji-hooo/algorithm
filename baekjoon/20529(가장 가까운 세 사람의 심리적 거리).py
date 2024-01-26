import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  mbti = list(map(str, input().split()))
  count = 10000
  if n > 32:
    count = 0
  else:
    for i in range(n - 2):
      for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
          x, y, z = mbti[i], mbti[j], mbti[k]
          tmp = 0
          for l in range(4):
            if x[l] != y[l]:
              tmp += 1
            if x[l] != z[l]:
              tmp += 1
            if y[l] != z[l]:
              tmp += 1
          count = min(count, tmp)
  print(count)