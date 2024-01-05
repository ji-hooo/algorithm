import sys
input = sys.stdin.readline

def wave(a):
  global p
  if a <= 5:
    return p[a]
  else:
    for i in range(6, a + 1):
      p.append(p[i - 5] + p[i - 1])
    return p[a]

for _ in range(int(input())):
  p = [0, 1, 1, 1, 2, 2]
  n = int(input())
  print(wave(n))