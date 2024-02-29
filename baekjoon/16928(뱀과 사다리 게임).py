import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0] * 101
visited = [0] * 101
visited[1] = 1

ladderSnake = dict()
for _ in range(n + m):
  x, y = map(int, input().split())
  ladderSnake[x] = y

def bfs():
  q = deque([1])
  while q:
    now = q.popleft()
    for move in range(1, 7):
      dmove = move + now
      if 0 < dmove <= 100 and visited[dmove] == 0:
        if dmove in ladderSnake.keys():
          dmove = ladderSnake[dmove]
        if visited[dmove] == 0:
          visited[dmove] = 1
          board[dmove] = board[now] + 1
          q.append(dmove)

bfs()

print(board[100])
