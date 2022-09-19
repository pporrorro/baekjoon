n = int(input())
str = ''

for i in range(n) :
  str += '*'  
  print('{0: >{1}}'.format(str, n))