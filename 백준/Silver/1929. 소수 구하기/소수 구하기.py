M, N = map(int, input().split())
lst = [0 for i in range(N+1)]

for i in range(2,N+1):
  if lst[i] == 0:
    for j in range(2*i,N+1,i):
      lst[j]=1
for ss in range(M,N+1):
  if lst[ss]==0 and ss!=1:
    print(ss)