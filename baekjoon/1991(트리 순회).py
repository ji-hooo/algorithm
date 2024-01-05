import sys
input = sys.stdin.readline

n = int(input())

graph = {}

for i in range(65, 65 + n):
  graph[chr(i)] = ['', '', '']

for _ in range(n):
  node, left, right = map(str, input().split())
  if left.isalpha():
    graph[node][1] = left
    graph[left][0] = node
  if right.isalpha():
    graph[node][2] = right
    graph[right][0] = node

def preOrder(a):
  if a:
    print(a, end = '')
    preOrder(graph[a][1])
    preOrder(graph[a][2])

def inOrder(a):
  if a:
    inOrder(graph[a][1])
    print(a, end = '')
    inOrder(graph[a][2])

def postOrder(a):
  if a:
    postOrder(graph[a][1])
    postOrder(graph[a][2])
    print(a, end = '')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
