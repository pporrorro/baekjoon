t = int(input())
cnt = 0

while t != cnt :
  cnt += 1
  a, b = map(int, input().split())
  print('Case #{0}: {1} + {2} = {3}'.format(cnt, a, b, a+b))