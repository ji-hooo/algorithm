n = int(input())

stars = [[" "] * (n) for _ in range(n)]

for i in range(n):
  for j in range(n-1, n-2-i, -1):
    stars[i][j] = "*"

for i in range(n):
  print("".join(stars[i]))