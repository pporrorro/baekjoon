c = int(input())
ts, nr = 0, 0, 

for _ in range(c) :
  slst = list(map(int,input().split()))
  sn = slst[0]
  ss = sum(slst[1:])

  for i in slst[1:]:
    if ss/sn < i :
      nr += 1
  an = nr/sn*100
  print('{0:.3f}%'.format(an))
  ts, nr = 0, 0