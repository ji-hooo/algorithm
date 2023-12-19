import sys
import math
input = sys.stdin.readline

m, n = map(int, input().split())

def isPrime(num):
  if num == 1:
    return False
  
  for i in range(2, int(math.sqrt(num)+1)):
    if num%i == 0:
      return False

  return True

for i in range(m, n + 1):
  if isPrime(i):
    print(i)

