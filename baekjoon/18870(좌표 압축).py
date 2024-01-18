import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arrSet = sorted(set(arr))
arrZip = {arrSet[i]: i for i in range(len(arrSet))}

for i in arr:
  print(arrZip[i], end = ' ')
