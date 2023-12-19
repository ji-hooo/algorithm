import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

arr = sorted([int(input()) for _ in range(n)])

arr_avg = round(sum(arr) / len(arr))

arr_mid = arr[len(arr)//2]

mode = Counter(arr)
mx = max(mode.values())
mode_max = []

for i in mode:
  if mode[i] == mx:
    mode_max.append(i)

arr_diff = max(arr) - min(arr)

print(arr_avg)
print(arr_mid)
print(mode_max[0]) if len(mode_max) == 1 else print(mode_max[1])
print(arr_diff)