T = int(input())
YY, XX = 0,0

for _ in range(T) :
  H, W, N = map(int, input().split())
  if N % H == 0  :
    XX = N // H
    YY = H
  else:
    XX = (N // H) + 1
    YY = N % H
  print(format(YY)+'{0:0>2}'.format(XX))