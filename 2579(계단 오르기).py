import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
maximum = [0] * (n + 1)

maximum[1] = stairs[1]

if n != 1:
  maximum[2] = max(stairs[1] + stairs[2], stairs[2])

for i in range(3, n + 1):
  maximum[i] = max(maximum[i - 3] + stairs[i - 1] + stairs[i], maximum[i - 2] + stairs[i])

print(maximum[n])