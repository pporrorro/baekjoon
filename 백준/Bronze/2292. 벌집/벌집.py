N = int(input())
s = 1
f = 1

while True :
  if N == s :
    break
  if s < N and N <= s + 6 * f:
    f += 1
    break 
  else :
    s += 6 * f
    f += 1

print( f )