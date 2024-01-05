from collections import deque

N, M, Y, X, K = map(int, input().split())

dice = {'TOP': 0, 'LEFT': 0, 'RIGHT': 0, 'FRONT': 0, 'BACK': 0, 'BOTTOM': 0}

def roll(direction):
  if direction == 0:
    dice["TOP"], dice["RIGHT"], dice["BOTTOM"], dice["LEFT"] = dice["RIGHT"], dice["BOTTOM"], dice["LEFT"], dice["TOP"]
  elif direction == 1:
    dice["TOP"], dice["LEFT"], dice["BOTTOM"], dice["RIGHT"] = dice["LEFT"], dice["BOTTOM"], dice["RIGHT"], dice["TOP"]
  elif direction == 2:
    dice["TOP"], dice["BACK"], dice["BOTTOM"], dice["FRONT"] = dice["BACK"], dice["BOTTOM"], dice["FRONT"], dice["TOP"]
  else:
    dice["TOP"], dice["FRONT"], dice["BOTTOM"], dice["BACK"] = dice["FRONT"], dice["BOTTOM"], dice["BACK"], dice["TOP"]

board = []

for _ in range(N):
  board.append(list(map(int, input().split())))

move = deque(map(int, input().split()))

dY = [0, 0 , -1, 1]
dX = [1, -1, 0, 0]

while move:
  nextDirection = move.popleft() - 1
  nY, nX = Y + dY[nextDirection], X + dX[nextDirection]
  if 0 <= nY < N and 0 <= nX < M:
    Y, X = nY, nX
    roll(nextDirection)
    if board[Y][X] != 0:
      dice["BOTTOM"] = board[Y][X]
      board[Y][X] = 0
    else:
      board[Y][X] = dice["BOTTOM"]

    print(dice["TOP"])

  else:
    continue