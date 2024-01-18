import sys
input = sys.stdin.readline

equation = input().rstrip()

sum = 0
tmp = 0
digit = 1

for i in range(len(equation) - 1, -1, -1):
  if equation[i] == '+':
    digit = 1
  elif equation[i] == '-':
    sum -= tmp
    tmp = 0
    digit = 1
  else:
    tmp += int(equation[i]) * digit
    digit = digit * 10

  if i == 0:
    sum += tmp
  
print(sum)