import sys
input = sys.stdin.readline

a, b = input().strip(), input().strip()
lcs = [''] * 1000

for i in range(len(a)):
  temp = ''
  for j in range(len(b)):
    if len(temp) < len(lcs[j]):
      temp = lcs[j]
    elif a[i] == b[j]:
      lcs[j] = temp + a[i]

print(max(map(lambda x: len(x), lcs)))