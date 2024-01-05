import sys
input = sys.stdin.readline

n = int(input())

lecture = list(map(int, input().split()))

pre_avg = sum(lecture) / len(lecture)

max_lecture = max(lecture)

for i in range(n):
  lecture[i] = lecture[i]/max_lecture * 100

post_avg = sum(lecture) / len(lecture)

print(post_avg)