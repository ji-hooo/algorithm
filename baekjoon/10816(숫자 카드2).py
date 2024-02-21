import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards_num = {}

m = int(input())
cardCount = list(map(int, input().split()))

for i in cards:
  if i in cards_num:
    cards_num[i] += 1
  else:
    cards_num[i] = 1

for i in range(m):
  if cardCount[i] in cards_num:
    print(cards_num[cardCount[i]], end = ' ')
  else:
    print(0, end = ' ')