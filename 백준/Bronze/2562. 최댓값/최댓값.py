nlst = list()

for _ in range(9) :
  nlst.append(int(input()))
print(max(nlst))
print(nlst.index(max(nlst)) + 1 )