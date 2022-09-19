n, x = map(int, input().split())
a = list(input().split())
s = ''

for i in a :
  if int(i) < x :
    s += '{0} '.format(i)
  
print(s)