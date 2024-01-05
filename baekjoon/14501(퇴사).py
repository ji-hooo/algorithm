N = int(input())

schedules = [list(map(int, input().split())) for _ in range(N)]

box = [0] * (N + 1)

for i in range(N-1, -1, -1):
  if i + schedules[i][0] > N:
    box[i] = box[i + 1]
  else:
    box[i] = max(box[i + 1], schedules[i][1] + box[i + schedules[i][0]])

print(box[0])