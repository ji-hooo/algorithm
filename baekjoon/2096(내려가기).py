import sys
input = sys.stdin.readline

n = int(input())

max_result = [0] * 3
min_result = [0] * 3

max_temp = [0] * 3
min_temp = [0] * 3

for i in range(n):
  a, b, c = map(int, input().split())
  for j in range(3):
    if j == 0:
      max_temp[j] = a + max(max_result[j], max_result[j + 1])
      min_temp[j] = a + min(min_result[j], min_result[j + 1])
    elif j == 1:
      max_temp[j] = b + max(max_result[j], max_result[j + 1], max_result[j - 1])
      min_temp[j] = b + min(min_result[j], min_result[j + 1], min_result[j - 1])
    else:
      max_temp[j] = c + max(max_result[j], max_result[j - 1])
      min_temp[j] = c + min(min_result[j], min_result[j - 1])
  
  for j in range(3):
    max_result[j] = max_temp[j]
    min_result[j] = min_temp[j]

print(max(max_result), min(min_result))