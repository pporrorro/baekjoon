M = int(input()) # 범위 최대값
N = int(input()) # 범위 최솟값
slist = list()

# 소수 구하기
for num in range(M,N+1):
  cnt = 0
  for i in range(1,num+1):
    if num % i == 0:
      cnt += 1 
  if cnt == 2:       # 오직 본인과 1  
    slist.append(num)

# 출력
if len(slist) == 0:
  print(-1)
else:
  print(sum(slist))
  print(min(slist))