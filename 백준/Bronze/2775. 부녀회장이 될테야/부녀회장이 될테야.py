T = int(input())
dir = {}
result = 0

for _ in range(1,T+1) :
  k = int(input())
  n = int(input())
  for a in range(0,k+1):
    for b in range(1,n+1) :
      if a == 0 :
        dir['{0}{1}'.format(a,b)] = b
      else : 
        for c in range(1,b+1):
          result += dir['{0}{1}'.format(a-1,c)]
        dir['{0}{1}'.format(a,b)] = result
        result = 0

  print(dir['{0}{1}'.format(k,n)])