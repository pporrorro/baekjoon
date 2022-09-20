c = int(input())
s, ts = 0, 0

for _ in range(c) :
  ox = input()
  for i in ox :
    if i == 'X':
      s = 0
    elif i == 'O' :
      s += 1 
    ts += s
  print(ts)
  s, ts = 0, 0 