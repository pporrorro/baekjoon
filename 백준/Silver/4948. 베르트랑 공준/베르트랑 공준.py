n = int(input())

while n != 0:
  li = [0 for i in range(2*n+1)] # 그놈의 체
  cnt = 0

  for i in range(2,2*n+1):
    if li[i] == 0:
      for j in range(2*i,2*n+1,i):
        li[j] = 1
  for i in range(2,len(li)):
    if i > n and i <= 2*n and li[i] == 0:
      cnt += 1
  print(cnt)
  n = int(input())