import sys
input = sys.stdin.readline

t = int(input())

def fibonacci(t):
  for i in range(t):
    n = int(input())
    zero = [1, 0]
    one = [0, 1]
    
    if n <= 40:
      for i in range(2, n + 1):
        zero.append(zero[i - 2] + zero[i - 1])
        one.append(one[i - 2] + one[i - 1])
  
    print ('%d %d'%(zero[n], one[n]))

fibonacci(t)
