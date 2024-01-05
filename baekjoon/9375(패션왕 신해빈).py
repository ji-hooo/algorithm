import sys
input = sys.stdin.readline

def count(x):
  clothes = {}
  for _ in range(x):
    a, b = map(str, input().split())
    if b in clothes:
      clothes[b] += 1 
    else:
      clothes[b] = 2
    
  result = 1
  for i in clothes.values():
    result *= i
  
  print(result - 1)

n = int(input())
for _ in range(n):
  count(int(input()))