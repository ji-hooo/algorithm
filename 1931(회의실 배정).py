import sys
input = sys.stdin.readline

n = int(input())

schedules = []
for i in range(n):
  a, b = map(int, input().split())
  schedules.append([b, a])

schedules.sort()

count = 1

end = schedules[0][0]
for i in range(1, n):
  if schedules[i][1] >= end:
    end = schedules[i][0]
    count += 1

print(count)