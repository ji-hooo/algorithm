import sys
from collections import deque

block_num = int(sys.stdin.readline())

apple_num = int(sys.stdin.readline())

board = [[0 for _ in range(block_num)] for _ in range(block_num)]

for _ in range(apple_num):
  y, x = map(int, sys.stdin.readline().split())
  board[y-1][x-1] = 2

rotationTime = {}
rotationNum = int(sys.stdin.readline())
for _ in range(rotationNum):
  sec, rotation = sys.stdin.readline().split()
  rotationTime[int(sec)] = rotation

board[0][0] = 1
direction = (0, 1)

def change_direction(direction, rotation):
  y, x = direction
  if y == 0:
    if rotation == 'D':
      if x > 0:
        return (1, 0)
      else:
        return (-1, 0)
    else:
      if x > 0:
        return (-1, 0)
      else:
        return (1, 0)
      
  elif x == 0:
    if rotation == 'D':
      if y > 0:
        return (0, -1)
      else:
        return (0, 1)
    else:
      if y > 0:
        return (0, 1)
      else:
        return (0, -1)

sec = 0
y, x = 0, 0

snake = deque()
snake.append((y, x))

while True:
  sec += 1
  dy, dx = direction
  nexty, nextx = y + dy, x + dx

  if 0 <= nexty < block_num and 0 <= nextx < block_num:
    if board[nexty][nextx] == 2:
      snake.appendleft((nexty, nextx))
      board[nexty][nextx] = 1

    elif board[nexty][nextx] == 0:
      snake.appendleft((nexty, nextx))
      board[nexty][nextx] = 1
      taily, tailx = snake.pop()
      board[taily][tailx] = 0

    elif board[nexty][nextx] == 1:
      break

    y, x = nexty, nextx

    if sec in rotationTime:
      direction = change_direction(direction, rotationTime[sec])

  else:
    break

print(sec)