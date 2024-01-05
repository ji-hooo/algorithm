import sys
input = sys.stdin.readline

n = int(input())

tree = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  for j in range(i + 1):
    if j == 0:
      tree[i][j] += tree[i - 1][0]
    elif j == i:
      tree[i][j] += tree[i -1][-1]
    else:
      tree[i][j] += max(tree[i - 1][j - 1], tree[i - 1][j])

print(max(tree[-1]))


