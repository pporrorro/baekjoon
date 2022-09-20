N = input()
nlist = map(int, input().split())
cnt = 0

for i in nlist :
  if i == 1 :
    continue
  cnt += 1
  for k in range(2, i) :
    if i % k == 0 :
      cnt -= 1
      break

print(cnt)