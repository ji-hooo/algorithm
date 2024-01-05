import sys
input = sys.stdin.readline

arr = [0, 1, 2, 4] + [0] * 7

for i in range(4, 11):
  arr[i] = sum(arr[i - 3 : i])

n = int(input())
for _ in range(n):
  print(arr[int(input())])