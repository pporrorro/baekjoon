n = int(input())
score = list(map(int,input().split()))
nscore = []

for i in score :
  m = max(score)
  nscore.append(i/m*100)

print(sum(nscore)/n)