n, m = map(int, input().split())
location = 0
board = []
location_num = 0

board.append(int(input()))

for i in range(n-2):
  board_instruction = int(input())
  board.append(board_instruction)

board.append(int(input()))

for i in range(m):
  dice_num = int(input())
  location_num += 1
  location += dice_num
  if location >= (len(board)-1):
    break
  location += board[location]
  if location >= (len(board)-1):
    break

print(location_num)