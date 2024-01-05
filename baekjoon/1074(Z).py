import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

length = 2 ** n
num = 0

while length:
  length //= 2
  if r < length and c < length:
    num += 0
  elif r < length and c >= length:
    num += length ** 2
    c -= length
  elif r >= length and c < length:
    num += (length ** 2) * 2
    r -= length
  else:
    num += (length ** 2) * 3
    c -= length
    r -= length

print (num)

