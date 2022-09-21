T = int(input())

while T > 0:
  n = int(input())
  li = [0 for i in range(n)]
  dic = {}

  for i in range(2,n):
    if li[i] == 0:
      for j in range(2*i,n,i):
        li[j] = 1
    if li[i] + li[n-i] == 0 and n-i >= i:
      dic = {i:n-i-i}
  min_n = min(dic.keys())
  print(min_n, n-min_n)
  T -= 1