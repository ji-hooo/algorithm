import math

N = int(input())

def isPrime(num):
  if num == 1:
    return False
  
  for i in range(2, int(math.sqrt(num)+1)):
    if num%i == 0:
      return False

  return True


for i in range(N, 1004000):
  if isPrime(i) == True and str(i) == str(i)[::-1]:
    print(i)
    break
  
