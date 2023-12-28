import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listen = set(input().rstrip() for _ in range(n))

listen_see = [a for _ in range(m) if (a := input().rstrip()) in listen]

print(len(listen_see), *sorted(listen_see), sep = '\n')