import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

preOrder = []

while True:
  try:
    a = int(input())
    preOrder.append(a)
  except:
    break

def result(start, end):
  if start > end:
    return
  else:
    mid = end + 1

    for i in range(start + 1, end + 1):
      if preOrder[i] > preOrder[start]:
        mid = i
        break
    
    result(start + 1, mid - 1)
    result(mid, end)
    print(preOrder[start])

result(0, len(preOrder) - 1)

# def result(preOrder):
#   if len(preOrder) == 0:
#     return

#   treeL, treeR = [], []
#   treeRoot = preOrder[0]

#   for i in range(1, len(preOrder)):
#     if preOrder[i] > treeRoot:
#       treeL = preOrder[1:i]
#       treeR = preOrder[i:]
#       break
#     else:
#       treeL = preOrder[1:]

#   result(treeL)
#   result(treeR)
#   print(treeRoot)
  

# result(preOrder)