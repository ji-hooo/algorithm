N = int(input())

abilities = [list(map(int, input().split())) for _ in range(N)]

redTeam = []
result = -1

for i in range(len(abilities)):
  for j in range(len(abilities)):
    abilities[i][j] += abilities[j][i]

def seq(a):
  global result
  if len(redTeam) == N//2:
    blueTeam = [i for i in range(N) if i not in redTeam]
    redAbility = 0
    blueAbility = 0

    for i in range(N//2):
      for j in range(i+1, N//2):
        redAbility += abilities[redTeam[i]][redTeam[j]]
        blueAbility += abilities[blueTeam[i]][blueTeam[j]]

    gap = abs(redAbility - blueAbility)

    if result == -1:
      result = gap
    elif result > gap: 
      result = gap

  for i in range(a, N):
    if i in redTeam:
      continue
    redTeam.append(i)
    seq(i)
    redTeam.pop()

seq(0)
print(result)




