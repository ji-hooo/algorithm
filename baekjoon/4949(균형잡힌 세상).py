import sys
input = sys.stdin.readline

parenthesis = {')': '(', ']': '['}

while True:
  sentence = str(input().rstrip())
  if sentence == '.':
    break

  stack = []
  for i in sentence:
    if i in parenthesis.values():
      stack.append(i)
    elif i in parenthesis.keys():
      if len(stack) == 0:
        stack.append(i)
        break
      elif stack[-1] == parenthesis[i]:
        stack.pop()
      elif stack[-1] != parenthesis[i]:
        stack.append(i)
  
  if len(stack) == 0:
    print('yes')
  else:
    print('no')
