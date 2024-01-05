import sys
input = sys.stdin.readline

dictionary = []

n = int(input())

for _ in range(n):
  dictionary.append(input().rstrip())

words = list(set(dictionary))
words.sort()
words.sort(key = lambda x : len(x))

for word in words:
  print(word)